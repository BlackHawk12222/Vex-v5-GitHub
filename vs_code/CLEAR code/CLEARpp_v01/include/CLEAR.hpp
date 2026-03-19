#ifndef CLEAR.hpp
#define CLEAR.hpp

#include "vex.h"
#include <unordered_map>
#include <string>

class clear{

    public:

    clear(vex::brain* Brain_input);

    void add(const char *code, const char *details);

    private:
    vex::brain* Brain;
    int index = 0;
    vex::timer logtimer = vex::timer();

    std::unordered_map<std::string , std::string> codes= {
        {"DS0", ":System DATA: System Startup.:"}
    };
};

#endif
