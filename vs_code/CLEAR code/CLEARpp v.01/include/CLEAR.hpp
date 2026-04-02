#ifndef CLEAR_HPP
#define CLEAR_HPP
#include "main.h"
#include <list>

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
    void init_motor_monitor(std::list<pros::Motor> motors);
    log();
};
#endif CLEAR_HPP