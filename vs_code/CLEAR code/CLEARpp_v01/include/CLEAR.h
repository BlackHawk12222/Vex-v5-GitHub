#ifndef CLEAR_H
#define CLEAR_H

#include <vex.h>
#include <string>
#include <map>
#include <vector>
#include <functional>

using namespace vex;

class Settings;
class Recording;
class Log;
class Strip_Log;

class Log {
public:
  class Capture {
  public:
    class System {
    public:
      System();
      void memoryuse();
      void modules();
      void control(competition &comp);

      std::map<std::string, std::string> modulelist;
      int memory;
      int memory_tolerance;
      bool aton;
      bool driver;
      bool comp_switch;
      bool field;
    } system;

    class Drivetrain {
    public:
      Drivetrain();
      void standerd(drivetrain &dt, const std::string &type);
      void six_motor(motor &front_left_motor, motor &front_right_motor,
                     motor &middle_left_motor, motor &middle_right_motor,
                     motor &back_left_motor, motor &back_right_motor);

      int drivetrain_temp_monitoring;
      int drivetrain_power_monitoring;
      std::map<int, int> drivetrain_disconnected;
      int drivetrain_current_monitoring;
    } drivetrain;

    class Smartport {
    public:
      Smartport();
      void motor(motor &motor_obj);
      void optical(optical &opticalsensor);
      void inertial(inertial &inertialsensor);
      void distance(distance &distancesensor);
      void rotation(rotation &rotationsensor);

      std::map<std::string,int> motor_temp_monitoring;
      std::map<std::string,int> motor_power_monitoring;
      std::map<std::string,bool> motor_disconnected;
      std::map<std::string,int> motor_current_monitoring;
      std::map<int,bool> optical_object;
      std::map<int,int> optical_color;
      std::map<int,bool> optical_connected;
      bool inertial_connected;
      bool inertial_calibrating;
      int inertial_axis_tolerance;
      int inertial_gyro_tolerance;
      double inertial_rotation_history;
      double inertial_roll_history;
      double inertial_pitch_history;
      double inertial_heading_history;
      double inertial_x_axis_history;
      double inertial_y_axis_history;
      double inertial_z_axis_history;
      std::map<int,bool> distance_connection;
      std::map<int,bool> distance_object;
      std::map<int,double> distance_history;
      std::map<int,bool> rotation_connection;
      std::map<int,double> rotation_angle_history;
      std::map<int,double> rotation_position_history;
    } smartport;

    class Threewire {
    public:
      Threewire();
      void digitalinput(digital_in &input);
      void analog(analog_in &input);
      void bumper(brake &bumpersensor);  // approximation
      void limit(limit &limitsensor);   // approximation
      void potentiometer(potentiometer &sensor);
      void pwm(pwm_out &input);

      std::map<int,int> digital_value;
      std::map<int,int> analog_value;
    } threewire;

    Capture();
    void battery();
    void controller(controller &controller1);
    void variable(const std::string &name, double value);

    std::map<std::string,int> variables;
    int battery_voltage_monitoring;
    int battery_capacity_monitoring;
    int battery_current_monitoring;
    int battery_watt_monitoring;

    int axis1, axis2, axis3, axis4;
    bool button_a, button_b, button_x, button_y;
    bool button_up, button_down, button_left, button_right;
    bool button_L1, button_L2, button_R1, button_R2;
  } capture;

  class Archive {
  public:
    Archive();
    void log();
    void recording(const std::string &recordingname);
    void index_history();
    void recall_log();
    void recall_recording(const std::string &name);
  } archive;

  Log();
  void add(const std::string &add_code, const std::string &add_details);
  void add_codes(const std::string &code_add, const std::string &decoded_text);
  void remove_codes(const std::string &code_remove);
  void edit_codes(const std::string &code_edit, const std::string &new_decoded_text);
  void clear();
  void table();
  void read();

  void logstart(std::vector<motor*> drivemotors, drivetrain *drivetrain_obj, const std::string &drivetraintype,
                controller *controller1, controller *controller2, competition *Comp,
                std::map<std::string,motor*> othermotors);
  void add_logstart(const std::string &funtion);

  void auto_start();
  void auto_start_loop();

  bool adding;
  std::string format;
  std::string cache;
  bool brainscreen;
  int tolrance;
  bool manual_control;
  bool printing;
  bool logging;
  std::string loop;
  int index;
  std::map<std::string,std::string> codes;
};

class Recording {
public:
  Recording();
  void start(const std::string &Aton);
  void stop(const std::string &Aton);
  void encode(const std::string &Aton, const std::string &right, const std::string &left,
              const std::string &other1start, const std::string &other1stop, const std::string &other1button,
              const std::string &other2start, const std::string &other2stop, const std::string &other2button,
              const std::string &other3start, const std::string &other3stop, const std::string &other3button,
              const std::string &other4start, const std::string &other4stop, const std::string &other4button,
              const std::string &other5start, const std::string &other5stop, const std::string &other5button,
              const std::string &other6start, const std::string &other6stop, const std::string &other6button);
  void run(const std::string &Aton);

  bool record;
  std::string Aton;
  std::vector<std::string> postlist;
  std::string poststring;
};

class Settings {
public:
  Settings();
  std::string changes;
  std::map<std::string,std::string> settings;
  std::map<std::string,std::string> default_settings_dictionary;
};

class Strip_Log {
public:
  Strip_Log();
  void Strip_CLEAR();
  void add(const std::string &entry);
  void start(std::vector<motor*> args);
};

extern Log log;
extern Recording recording;
extern Settings settings;
extern Strip_Log logs;

#endif // CLEAR_H
