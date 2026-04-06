#ifndef CLEAR_HPP
#define CLEAR_HPP
#include "main.h"
#include <list>
#include <unordered_map>

class capture{
    public:
        void init_motor_monitor(std::list<pros::Motor> motors);
        void update_motor_monitor(std::list<pros::Motor> motors);
        void update_motor_temps(pros::Motor motor);
        void update_motor_power(pros::Motor motor);
        void update_motor_current(pros::Motor motor);
        void update_motor_efficiency(pros::Motor motor);
        capture();
    private:

        std::vector<short unsigned int> motor_monitor_temp;
        std::vector<short unsigned int> motor_monitor_current;
        std::vector<short unsigned int> motor_monitor_power;
        std::vector<short unsigned int> motor_monitor_efficiency;
        std::vector<short unsigned int> id_motor;
        
};

class logging{
 public:   
    void add(const char* Code, const char* Details);
    void log_start(std::list<pros::Motor> motors);
    void auto_start();
    logging();

 private:
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
};

#endif