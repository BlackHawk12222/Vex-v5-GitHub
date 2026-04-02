#ifndef CLEAR_HPP
#define CLEAR_HPP
#include "main.h"
#include <list>
#include <unordered_map>

class log{
 public:   
    void add(const char* Code, const char* Details);
    void log_start(std::list<pros::Motor> motors);
    void auto_start();

 private:
    std::list<short unsigned int> motor_monitor_temp;
    std::list<short unsigned int> motor_monitor_power;
    std::list<short unsigned int> motor_monitor_current;
    std::list<short unsigned int> motor_monitor_power;
    std::list<short unsigned int> motor_monitor_efficiency;
    long unsigned int index = 0;
    std::unordered_map<std::string, std::string> log_codes={
        {"MD01", "Motor DATA: Temps Normal. Temps: "},
        {"MD02", "Motor DATA: Power Normal. Power: "},
        {"MD03", "Motor DATA: Current Normal. Current: "},
        {"MD04", "Motor DATA: Efficiency Normal. Efficiency: "},
        {"MW01", "Motor WARNING: Temps High. Temps: "},
        {"MW02", "Motor WARNING: Power High. Power: "},
        {"MW03", "Motor WARNING: Current High. Current: "},
        {"MW04", "Motor WARNING: Efficiency Low. Efficiency: "},
        {"ME01", "Motor ERROR: Temps Critical. Temps: "},
        {"ME02", "Motor ERROR: Power Critical. Power: "},
        {"ME03", "Motor ERROR: Current Critical. Current: "},
        {"ME04", "Motor ERROR: Efficiency Critical. Efficiency: "},
    };
    void init_motor_monitor(std::list<pros::Motor> motors);
    void update_motor_monitor(std::list<pros::Motor> motors);
    void update_motor_temps(pros::Motor motor);
    void update_motor_power(pros::Motor motor);
    void update_motor_current(pros::Motor motor);
    void update_motor_efficiency(pros::Motor motor);
    log();
};
#endif CLEAR_HPP