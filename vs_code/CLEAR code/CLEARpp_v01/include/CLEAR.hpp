#ifndef CLEAR.hpp
#define CLEAR.hpp

#include "vex.h"
#include <unordered_map>
#include <string>

class clear{

    public:

    clear(vex::brain* Brain_input);

    void add(const char *code, const char *details);

    void start(vex::motor Right1, vex::motor Left1, vex::motor Right2, vex::motor Left2, vex::motor Right3, vex::motor Left3);

    private:
    vex::brain* Brain;
    int index = 0;
    vex::timer logtimer = vex::timer();

    std::unordered_map<std::string , std::string> codes= {
        {"DS0", ":System DATA: System Startup.:"},
        {"DS1", ":System DATA: System Stopped.:"}
    };
};

#endif
