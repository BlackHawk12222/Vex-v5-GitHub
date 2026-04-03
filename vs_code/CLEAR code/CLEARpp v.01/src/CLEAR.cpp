#include "main.h"
#include <list>
#include "CLEAR.hpp"
#include <unordered_map>

void logging::add(const char* Code, const char* Details){
    std::uint32_t time = pros::millis();
    std::string log_message = "[" + std::to_string(time) + "] " + log_codes[Code] + Details;
    printf("%s\n", log_message.c_str());
    FILE* log_file = fopen("/usd/log.txt", "a");
    if (log_file != nullptr) {
        fprintf(log_file, "%s\n", log_message.c_str());
        fclose(log_file);
    } else {
        printf("Error opening log file for writing.\n");
    }
    fclose(log_file);
}

void capture::init_motor_monitor(std::list<pros::Motor> motors){
    for (pros::Motor motor : motors){
            motor_monitor_temp.push_back(motor.get_temperature());
            motor_monitor_power.push_back(motor.get_power());
            motor_monitor_current.push_back(motor.get_current_draw());
            motor_monitor_efficiency.push_back(motor.get_efficiency());
            id_motor.push_back(motor.get_port());
        
    }
}

void capture::update_motor_temps(pros::Motor motor){
    unsigned short int temps=motor.get_temperature();
    for (int i=0; i<id_motor.size(); i++){
        if (id_motor[i]==motor.get_port()){
            if (temps != motor_monitor_temp[i]){
                if (temps>70){
                    Log->add("ME01", "");
                }
                else if (temps>50){
                    Log->add("MW01", "");
                }
                else{
                    Log->add("MD01", "");
                }
                motor_monitor_temp[i]=temps;
                break;
            }
        }
    }
}

void capture::update_motor_monitor(std::list<pros::Motor> motors){
    for (pros::Motor motor : motors){
        capture::update_motor_current(motor);
        capture::update_motor_efficiency(motor);
        capture::update_motor_power(motor);
        capture::update_motor_temps(motor);
    }
}

void logging::log_start(std::list<pros::Motor> motors){
    Capture->init_motor_monitor(motors);
    while (true){
        std::uint32_t time_start = pros::millis();
        Capture->update_motor_monitor(motors);
        std::uint32_t time_end = pros::millis();
        pros::delay(200- (time_end - time_start));
    }
}