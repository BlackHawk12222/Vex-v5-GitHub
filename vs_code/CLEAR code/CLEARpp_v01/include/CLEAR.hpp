#ifndef CLEAR.hpp
#define CLEAR.hpp

#include "vex.h"
#include <unordered_map>
#include <string>
#include <cstdio>
#include <iostream>

class clear{

    public:

    clear(vex::brain* Brain_input);

    void add(const char *code, const char *details);

    void start(vex::motor Right1, vex::motor Left1, vex::motor Right2, vex::motor Left2, vex::motor Right3, vex::motor Left3);

    private:
    vex::brain* Brain;
    int index = 0;
    vex::timer logtimer = vex::timer();
    short unsigned int  temp_monitoring = 0;
    short unsigned int power_moitoring = 0;
    bool disconnect_monitoring[6] = {false, false, false, false, false, false};

    void DrivetarinSixMotor(vex::motor Right1, vex::motor Left1, vex::motor Right2, vex::motor Left2, vex::motor Right3, vex::motor Left3);

    std::unordered_map<std::string , std::string> codes= {
        {"DS0", ":System DATA: System Startup.: "},
        {"DS1", ":System DATA: System Stopped.: "},
        {"ED0", ":Drivetrain ERROR: Critical Temps. Highest Temp: "},
        {"WD0", ":Drivetrain WARNING: High Temps. Highest Temp: "},
        {"DD0", ":Drivetrain DATA: Normal Temps. Highest Temp: "},
        {"ED1", ":Drivetrain ERROR: Critical Power. Peak Power: "},
        {"WD1", ":Drivetrain WARNING: High Power. Peak Power: "},
        {"DD1", ":Drivetrain DATA: Normal Power. Peak Power: "},
        {"ED2", ":Drivetrain ERROR: Motor Diconnected. Motor: "},
        {"ED2", ":Drivetrain DATA: Motor Connected. Motor: "},
    };
};

#endif
