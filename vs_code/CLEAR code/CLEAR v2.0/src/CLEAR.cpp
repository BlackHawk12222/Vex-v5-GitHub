#include "CLEAR.h"
#include <fstream>
#include <sstream>

using namespace vex;

// Global instances
Log log;
Recording recording;
Settings settings;
Strip_Log logs;

// --- Capture::System ---
Log::Capture::System::System()
  : memory(0), memory_tolerance(100), aton(false), driver(false), comp_switch(false), field(false) {}

void Log::Capture::System::memoryuse() {
  // VEX API does not expose memory alloc in same way. stub.
}

void Log::Capture::System::modules() {
  // Python sys.modules mapping not available
}

void Log::Capture::System::control(competition &comp) {
  if (comp.is_autonomous() && !aton) {
    log.add_codes("DSC0", ":Competition DATA: Autonomous Started:");
    log.add("DSC0", "");
    aton = true; driver = false;
  }
  if (comp.is_driver_control() && !driver) {
    log.add_codes("DSC1", ":Competition DATA: Driver Control Started:");
    log.add("DSC1", "");
    driver = true; aton = false;
  }
  if (comp.is_competition_switch() && !comp_switch) {
    log.add_codes("DSC2", ":Competition DATA: Competition Connected:");
    log.add("DSC2", "");
    comp_switch = true;
  }
  if (comp.is_field_control() && !field) {
    log.add_codes("DSC3", ":Competition DATA: Field Connected:");
    log.add("DSC3", "");
    field = true;
  } else if (!comp.is_field_control() && field) {
    log.add_codes("DSC4", ":Competition DATA: Field Disconnected:");
    log.add("DSC4", "");
    field = false;
  }
}

// --- Capture::Drivetrain ---
Log::Capture::Drivetrain::Drivetrain()
  : drivetrain_temp_monitoring(0), drivetrain_power_monitoring(0), drivetrain_current_monitoring(0) {}

void Log::Capture::Drivetrain::standerd(drivetrain &dt, const std::string &type) {
  // stub: no direct conversion for DriveTrain methods in C++ API in same names.
}

void Log::Capture::Drivetrain::six_motor(motor &front_left_motor, motor &front_right_motor,
                                         motor &middle_left_motor, motor &middle_right_motor,
                                         motor &back_left_motor, motor &back_right_motor) {
  // stub: monitor values and log if thresholds exceed.
}

// --- Capture::Smartport ---
Log::Capture::Smartport::Smartport()
  : inertial_connected(true), inertial_calibrating(false), inertial_axis_tolerance(50), inertial_gyro_tolerance(5),
    inertial_rotation_history(0), inertial_roll_history(0), inertial_pitch_history(0), inertial_heading_history(0),
    inertial_x_axis_history(0), inertial_y_axis_history(0), inertial_z_axis_history(0) {}

void Log::Capture::Smartport::motor(motor &motor_obj) {
  std::string motor_id = std::to_string(reinterpret_cast<uintptr_t>(&motor_obj));
  if (motor_temp_monitoring.find(motor_id) == motor_temp_monitoring.end()) {
    motor_temp_monitoring[motor_id] = 0;
    motor_power_monitoring[motor_id] = 0;
    motor_current_monitoring[motor_id] = 0;
    motor_disconnected[motor_id] = false;
  }

  int motor_temp = motor_obj.temperature(pct);
  if (motor_temp > 70) {
    if (motor_temp_monitoring[motor_id] != 1) {
      log.add("EM0", "Motor " + motor_obj.name() + " Temp " + std::to_string(motor_temp));
      motor_temp_monitoring[motor_id] = 1;
    }
  } else if (motor_temp > 50) {
    if (motor_temp_monitoring[motor_id] == 0) {
      log.add("WM0", "Motor " + motor_obj.name() + " Temp " + std::to_string(motor_temp));
      motor_temp_monitoring[motor_id] = 2;
    }
  } else {
    if (motor_temp_monitoring[motor_id] != 0) {
      log.add("DM0", "Motor " + motor_obj.name() + " Temp " + std::to_string(motor_temp));
      motor_temp_monitoring[motor_id] = 0;
    }
  }
}

void Log::Capture::Smartport::optical(optical &opticalsensor) {
  int oid = reinterpret_cast<int>(opticalsensor.installed()); // placeholder
  if (optical_connected.find(oid) == optical_connected.end()) {
    optical_connected[oid] = opticalsensor.installed();
    optical_object[oid] = false;
    optical_color[oid] = 0;
  }
  // stub: sensor conditions
}

void Log::Capture::Smartport::inertial(inertial &inertialsensor) {
  if (inertialsensor.isInstalled()) {
    if (!inertial_connected) {
      log.add_codes("DI7", ":Inertial DATA: Inertial Installed:");
      log.add("DI7", "");
      inertial_connected = true;
    }
    if (inertialsensor.isCalibrating() && !inertial_calibrating) {
      log.add_codes("DI2", ":Inertial DATA: Calibrating:");
      log.add("DI2", "");
      inertial_calibrating = true;
    } else if (!inertialsensor.isCalibrating() && inertial_calibrating) {
      log.add_codes("DI3", ":Inertial DATA: Calibration Complete:");
      log.add("DI3", "");
      inertial_calibrating = false;
    }

    double rotation = inertialsensor.rotation();
    if (std::abs(rotation - inertial_rotation_history) > inertial_gyro_tolerance) {
      log.add_codes("DI0", ":Inertial DATA: Rotation Changed. Rotation:");
      log.add("DI0", std::to_string(rotation));
      inertial_rotation_history = rotation;
    }
    // rest sensors similarly...
  } else {
    if (inertial_connected) {
      log.add_codes("EI0", ":Inertial ERROR: Inertial Disconnected:");
      log.add("EI0", "");
      inertial_connected = false;
    }
  }
}

void Log::Capture::Smartport::distance(distance &distancesensor) {
  // stub - mapping not available in native vexass
}

void Log::Capture::Smartport::rotation(rotation &rotationsensor) {
  // stub
}

// --- Capture::Threewire ---
Log::Capture::Threewire::Threewire() {}

void Log::Capture::Threewire::digitalinput(digital_in &input) {
  int idv = reinterpret_cast<int>(&input);
  if (!digital_value.count(idv)) digital_value[idv]=0;
  if (input.value() && digital_value[idv]==0) {
    log.add_codes("DDI0", ":Digital DATA: Value High:");
    log.add("DDI0", "");
    digital_value[idv]=1;
  } else if (!input.value() && digital_value[idv]==1) {
    log.add_codes("DDI1", ":Digital DATA: Value Low:");
    log.add("DDI1", "");
    digital_value[idv]=0;
  }
}

void Log::Capture::Threewire::analog(analog_in &input) {
  int idv = reinterpret_cast<int>(&input);
  if (!analog_value.count(idv)) analog_value[idv]=0;
  int val = input.value();
  if (std::abs(val - analog_value[idv]) > 3) {
    log.add_codes("DAI0", ":Analog DATA: Value Changed. Value:");
    log.add("DAI0", std::to_string(val));
    analog_value[idv]=val;
  }
}

void Log::Capture::Threewire::bumper(brake &bumpersensor) {
  // placeholder
}

void Log::Capture::Threewire::limit(limit &limitsensor) {
  // placeholder
}

void Log::Capture::Threewire::potentiometer(potentiometer &sensor) {
  int idv = reinterpret_cast<int>(&sensor);
  if (!analog_value.count(idv)) analog_value[idv]=0;
  int angle = sensor.angle(vex::rotationUnits::deg);
  if (std::abs(angle - analog_value[idv]) > 3) {
    log.add_codes("DP0", ":Potentiometer DATA: Value Changed. Value:");
    log.add("DP0", std::to_string(angle));
    analog_value[idv] = angle;
  }
}

void Log::Capture::Threewire::pwm(pwm_out &input) {
  // placeholder
}

// --- Capture ---
Log::Capture::Capture()
  : battery_voltage_monitoring(0), battery_capacity_monitoring(0), battery_current_monitoring(0), battery_watt_monitoring(0),
    axis1(0), axis2(0), axis3(0), axis4(0), button_a(true), button_b(true), button_x(true), button_y(true),
    button_up(true), button_down(true), button_left(true), button_right(true), button_L1(true), button_L2(true), button_R1(true), button_R2(true) {
}

void Log::Capture::battery() {
  int voltage = brain.battery.capacity(); // approximate
  if (voltage < 12) {
    log.add("WB0", std::to_string(voltage));
  }
}

void Log::Capture::controller(controller &controller1) {
  int c_axis1 = controller1.Axis1.position();
  if (c_axis1 != axis1) {
    log.add("DC1", "Controller Axis1 " + std::to_string(c_axis1));
    axis1 = c_axis1;
  }
  // other axes and buttons simplified
}

void Log::Capture::variable(const std::string &name, double value) {
  if (!variables.count(name) || variables[name] != static_cast<int>(value)) {
    log.add("DV0", "Variable " + name + " Value " + std::to_string(value));
    variables[name] = static_cast<int>(value);
  }
}

// --- Archive ---
Log::Archive::Archive() {}

void Log::Archive::log() {
  log.add("DS1", "Archive log invoked");
}

void Log::Archive::recording(const std::string &recordingname) {
  log.add("DS3", recordingname);
}

void Log::Archive::index_history() {
  log.add("DS2", "Index history executed");
}

void Log::Archive::recall_log() {
  log.add("DS5", "Recall log");
}

void Log::Archive::recall_recording(const std::string &name) {
  log.add("DS5", name);
}

// --- Log ---
Log::Log() : index(0), adding(true), format("utf-8"), cache(""), brainscreen(false), tolrance(3), manual_control(false), printing(true), logging(true), loop("") {
  // Initialize codes list
  codes["ED1"] = ":Drivetrain ERROR: Motor(s) Critically Hot. Temp: ";
  codes["WB0"] = ":Battery WARNING: Low Voltage. Voltage: ";
  codes["DC1"] = ":Controller DATA: Axis Changed. Axis: ";

  // ensure file exists
  if (!brain.sdcard.isInserted()) return;
  if (!brain.sdcard.exists("Log.csv")) {
    brain.sdcard.savefile("Log.csv", std::vector<uint8_t>{'L','o','g',' ','S','t','a','r','t',':',' ','\n'});
  }
}

void Log::add(const std::string &add_code, const std::string &add_details) {
  if (!adding) return;
  std::string code = codes.count(add_code) ? codes[add_code] : ":Code ERROR: Not Found. Code: " + add_code;
  std::ostringstream entry;
  entry << ", " << index << " [" << brain.timerValue(timeUnits::msec) << "] " << code << " " << add_details << "\n";

  if (printing) {
    brain.Screen.print(entry.str().c_str());
  }

  if (logging) {
    std::string data = entry.str();
    std::vector<uint8_t> bytes(data.begin(), data.end());
    brain.sdcard.appendfile("Log.csv", bytes);
  }

  if (brainscreen) {
    brain.Screen.print(entry.str().c_str());
    brain.Screen.newLine();
  }

  ++index;
}

void Log::add_codes(const std::string &code_add, const std::string &decoded_text) {
  codes[code_add] = decoded_text;
}

void Log::remove_codes(const std::string &code_remove) {
  if (codes.count(code_remove)) codes.erase(code_remove);
}

void Log::edit_codes(const std::string &code_edit, const std::string &new_decoded_text) {
  if (codes.count(code_edit)) codes[code_edit] = new_decoded_text;
}

void Log::clear() {
  if (brain.sdcard.isInserted()) {
    brain.sdcard.savefile("Log.csv", std::vector<uint8_t>{'L','o','g',' ','S','t','a','r','t',':',' ','\n'});
  }
}

void Log::table() {
  for (auto &p : codes) {
    brain.Screen.print("%s -> %s\n", p.first.c_str(), p.second.c_str());
  }
}

void Log::read() {
  if (!brain.sdcard.isInserted()) return;
  auto content = brain.sdcard.loadfile("Log.csv");
  std::string decoded(content.begin(), content.end());
  brain.Screen.print(decoded.c_str());
}

void Log::logstart(std::vector<motor*> drivemotors, drivetrain *drivetrain_obj, const std::string &drivetraintype,
                   controller *controller1, controller *controller2, competition *Comp,
                   std::map<std::string,motor*> othermotors) {
  adding = true;
  manual_control = true;
  if (brainscreen) brain.Screen.setFont(mono12);

  archive.log();
  archive.index_history();
  add("DS0", "");

  while (true) {
    for (int i = 0; i < 20; ++i) {
      if (!recording.record) capture.battery();
      if (controller1) capture.controller(*controller1);
      if (controller2 && !recording.record) capture.controller(*controller2);
      if (Comp) capture.system.control(*Comp);
      if (drivetrain_obj) capture.drivetrain.standerd(*drivetrain_obj, drivetraintype);
      else if (!drivemotors.empty()) capture.drivetrain.six_motor(*drivemotors[0], *drivemotors[1], *drivemotors[2], *drivemotors[3], *drivemotors[4], *drivemotors[5]);

      for (auto &p : othermotors) capture.smartport.motor(*p.second);

      task::sleep(200);
    }
  }
}

void Log::add_logstart(const std::string &funtion) {
  std::string bytes(funtion + ", ");
  std::vector<uint8_t> data(bytes.begin(), bytes.end());
  brain.sdcard.appendfile("Logstart.txt", data);
}

void Log::auto_start_loop() {
  archive.log();
  archive.index_history();
  add("DS0", "");

  while (true) {
    if (!recording.record) capture.battery();
    task::sleep(200);
  }
}

void Log::auto_start() {
  auto_start_loop();
}

void Recording::Recording() : record(false), Aton(""), postlist(), poststring("") {}

void Recording::start(const std::string &AtonName) {
  std::string filename = AtonName + "_pre.txt";
  if (!record) {
    record = true;
    Aton = filename;
    log.add("DA0", filename);
  }
}

void Recording::stop(const std::string &AtonName) {
  record = false;
  log.add("DA1", AtonName + "_pre.txt");
}

void Recording::encode(const std::string &Aton, const std::string &right, const std::string &left,
                        const std::string &other1start, const std::string &other1stop, const std::string &other1button,
                        const std::string &other2start, const std::string &other2stop, const std::string &other2button,
                        const std::string &other3start, const std::string &other3stop, const std::string &other3button,
                        const std::string &other4start, const std::string &other4stop, const std::string &other4button,
                        const std::string &other5start, const std::string &other5stop, const std::string &other5button,
                        const std::string &other6start, const std::string &other6stop, const std::string &other6button) {
  log.add("DA2", Aton + ".txt");
}

void Recording::run(const std::string &AtonName) {
  log.add("DA3", AtonName + ".txt");
}

Settings::Settings() {
  default_settings_dictionary = {
    {"brain_read", "False"},
    {"print_read", "True"},
    {"sdcard_read", "True"},
    {"gc_use", "True"},
    {"archive_log", "True"},
    {"archive_recordings", "True"},
    {"log_memory", "False"},
    {"log_modules", "True"},
    {"log_battery", "True"},
    {"logging_loop_wait", "200"},
    {"recording_loop_wait", "0"},
    {"format_used", "utf-8"},
    {"auto_do_motors", "True"},
    {"auto_do_variables", "True"},
    {"auto_do_control", "True"},
    {"auto_do_three_wire", "True"},
    {"auto_do_smart_port", "True"},
    {"auto_do_controller", "True"},
    {"default_tolrance", "3"},
    {"memory_tolrance_KB", "100"},
    {"distance_tolrance_MM", "100"},
    {"inertial_gyro_tolrance_DEGREES", "5"},
    {"inertial_axis_tolrance_Gs", "0.5"}
  };

  if (brain.sdcard.isInserted() && !brain.sdcard.exists("settings.txt")) {
    std::ostringstream contents;
    for (auto &p : default_settings_dictionary) {
      contents << p.first << " : " << p.second << "\n";
      settings[p.first] = p.second;
    }
    std::string bytes = contents.str();
    brain.sdcard.savefile("settings.txt", std::vector<uint8_t>(bytes.begin(), bytes.end()));
  } else if (brain.sdcard.exists("settings.txt")) {
    auto data = brain.sdcard.loadfile("settings.txt");
    std::string decoded(data.begin(), data.end());
    std::istringstream iss(decoded);
    std::string line;
    while (std::getline(iss, line)) {
      auto pos = line.find(":");
      if (pos != std::string::npos) {
        std::string key = line.substr(0,pos);
        std::string value = line.substr(pos+1);
        settings[key] = value;
      }
    }
  }
}

Strip_Log::Strip_Log() {}

void Strip_Log::Strip_CLEAR() {
  // in C++ we cannot delete global values similarly.
}

void Strip_Log::add(const std::string &entry) {
  brain.Screen.print(entry.c_str());
  std::string s = entry + "\n";
  brain.sdcard.appendfile("Strip_Log.txt", std::vector<uint8_t>(s.begin(), s.end()));
}

void Strip_Log::start(std::vector<motor*> args) {
  while (true) {
    for (auto m : args) {
      std::ostringstream out;
      out << "Motor: " << m->name() << ", Position: " << m->position(deg) << ", Velocity: " << m->velocity(pct)
          << ", Temperature: " << m->temperature(pct);
      add(out.str());
    }
    task::sleep(200);
  }
}
