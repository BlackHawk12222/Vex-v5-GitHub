#include "vex.h"
#include <unordered_map>
#include <string>
#include <cstdio>
#include <iostream>
#include "CLEAR.hpp"



clear::clear(vex::brain* Brain_input){
    Brain = Brain_input;
    if (!(Brain->SDcard.exists("Log.csv"))){
        uint8_t buffer[] = "Log start: \n";
        Brain->SDcard.savefile("Log.csv", buffer, sizeof(buffer));
    }
}

void clear::add(const char *code, const char *details){
    int time_of_log = logtimer.time(vex::timeUnits::msec);
    std::string body_log = codes.at(code);
    Brain-> Screen.print(", %d [%d] %s %s \n", index, time_of_log, body_log.c_str(), details);
    if (Brain-> SDcard.isInserted()){
        int buffersize = snprintf(nullptr, 0, ", %d [%d] %s %s \n", index, time_of_log, body_log.c_str(), details);
        char buffer[buffersize];
        snprintf(buffer, buffersize + 1, ", %d [%d] %s %s \n", index, time_of_log, body_log.c_str(), details);
        Brain-> SDcard.appendfile("Log.csv", (uint8_t*)buffer, sizeof(buffer));
    }
    index+=1;
}

void start(){
    clear* Clear;
    Clear->add("DS0", "");
    while(true){
        vex::wait(5, vex::msec);
    };
}