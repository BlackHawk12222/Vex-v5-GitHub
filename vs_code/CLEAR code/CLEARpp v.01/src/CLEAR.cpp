#include "main.h"
#include <list>
#include "CLEAR.hpp"
#include <unordered_map>

void log::add(const char* Code, const char* Details){
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

void log::init_motor_monitor(std::list<pros::Motor> motors){
    for (pros::Motor motor : motors){
            motor_monitor_temp.push_back(motor.get_temperature());
            motor_monitor_power.push_back(motor.get_power());
            motor_monitor_current.push_back(motor.get_current_draw());
            motor_monitor_efficiency.push_back(motor.get_efficiency());
        
    }
}

void log::update_motor_temps(pros::Motor motor){
    unsigned short int temps=motor.get_temperature();
    if (temps>70){
        log::add("ME01", "");
    }
}

void log::update_motor_monitor(std::list<pros::Motor> motors){
    for (pros::Motor motor : motors){
        log::update_motor_current(motor);
        log::update_motor_efficiency(motor);
        log::update_motor_power(motor);
        log::update_motor_temps(motor);
    }
}

void log::log_start(std::list<pros::Motor> motors){
    init_motor_monitor(motors);
    while (true){
        std::uint32_t time_start = pros::millis();
        update_motor_monitor(motors);
        std::uint32_t time_end = pros::millis();
        pros::delay(200- (time_end - time_start));
    }
}