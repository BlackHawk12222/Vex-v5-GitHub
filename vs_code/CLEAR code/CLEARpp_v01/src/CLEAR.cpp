#include "vex.h"
#include <algorithm>
#include "CLEAR.hpp"
#include <typeinfo>
#include <string>



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
    Brain->Screen.newLine();
    int buffersize = snprintf(nullptr, 0, ", %d [%d] %s %s \n", index, time_of_log, body_log.c_str(), details);
    char buffer[buffersize];
    snprintf(buffer, buffersize + 1, ", %d [%d] %s %s \n", index, time_of_log, body_log.c_str(), details);
    if (Brain-> SDcard.isInserted()){
        Brain-> SDcard.appendfile("Log.csv", (uint8_t*)buffer, sizeof(buffer));  
    }
    printf("%s", buffer);
    index+=1;
}

void clear::DrivetarinSixMotor(vex::motor Right1, vex::motor Left1, vex::motor Right2, vex::motor Left2, vex::motor Right3, vex::motor Left3){

    
    if ((Right1.temperature(vex::percent) > 70 || Right2.temperature(vex::percent) > 70 || Right3.temperature(vex::percent) > 70 || Left1.temperature(vex::percent) > 70 || Left2.temperature(vex::percent) > 70 || Left3.temperature(vex::percent) > 70) && clear::temp_monitoring < 1){
        short int buffersize = snprintf(nullptr, 0, "%.2f", std::max({Right1.temperature(vex::percent), Right2.temperature(vex::percent), Right3.temperature(vex::percent), Left1.temperature(vex::percent), Left2.temperature(vex::percent), Left3.temperature(vex::percent)}));
        char buffer[buffersize];
        snprintf(buffer, buffersize + 1, "%.2f", std::max({Right1.temperature(vex::percent), Right2.temperature(vex::percent), Right3.temperature(vex::percent), Left1.temperature(vex::percent), Left2.temperature(vex::percent), Left3.temperature(vex::percent)}));
        clear::add("ED0", buffer);
        clear::temp_monitoring = 1;
    }
    else if ((Right1.temperature(vex::percent) > 50 || Right2.temperature(vex::percent) > 50 || Right3.temperature(vex::percent) > 50 || Left1.temperature(vex::percent) > 50 || Left2.temperature(vex::percent) > 50 || Left3.temperature(vex::percent) > 50) && clear::temp_monitoring < 2){
        short int buffersize = snprintf(nullptr, 0, "%.2f", std::max({Right1.temperature(vex::percent), Right2.temperature(vex::percent), Right3.temperature(vex::percent), Left1.temperature(vex::percent), Left2.temperature(vex::percent), Left3.temperature(vex::percent)}));
        char buffer[buffersize];
        snprintf(buffer, buffersize + 1, "%.2f", std::max({Right1.temperature(vex::percent), Right2.temperature(vex::percent), Right3.temperature(vex::percent), Left1.temperature(vex::percent), Left2.temperature(vex::percent), Left3.temperature(vex::percent)}));
        clear::add("WD0", buffer);
        clear::temp_monitoring = 2;
    }
    else if ((Right1.temperature(vex::percent) <= 50 || Right2.temperature(vex::percent) <= 50 || Right3.temperature(vex::percent) <= 50 || Left1.temperature(vex::percent) <= 50 || Left2.temperature(vex::percent) <= 50 || Left3.temperature(vex::percent) <= 50) && clear::temp_monitoring > 0){
        short int buffersize = snprintf(nullptr, 0, "%.2f", std::max({Right1.temperature(vex::percent), Right2.temperature(vex::percent), Right3.temperature(vex::percent), Left1.temperature(vex::percent), Left2.temperature(vex::percent), Left3.temperature(vex::percent)}));
        char buffer[buffersize];
        snprintf(buffer, buffersize + 1, "%.2f", std::max({Right1.temperature(vex::percent), Right2.temperature(vex::percent), Right3.temperature(vex::percent), Left1.temperature(vex::percent), Left2.temperature(vex::percent), Left3.temperature(vex::percent)}));
        clear::add("DD0", buffer);
        clear::temp_monitoring = 0;
    }

    if ((Right1.power(vex::watt) > 20 || Right2.power(vex::watt) > 20 || Right3.power(vex::watt) > 20 || Left1.power(vex::watt) > 20 || Left2.power(vex::watt) > 20 || Left3.power(vex::watt) > 20) && clear::power_moitoring < 1){
        short int buffersize = snprintf(nullptr, 0, "%.2f", std::max({Right1.power(vex::watt), Right2.power(vex::watt), Right3.power(vex::watt), Left1.power(vex::watt), Left2.power(vex::watt), Left3.power(vex::watt)}));
        char buffer[buffersize];
        snprintf(buffer, buffersize + 1, "%.2f", std::max({Right1.power(vex::watt), Right2.power(vex::watt), Right3.power(vex::watt), Left1.power(vex::watt), Left2.power(vex::watt), Left3.power(vex::watt)}));
        clear::add("ED1", buffer);
        clear::power_moitoring = 1;
    }  
    else if ((Right1.power(vex::watt) > 11 || Right2.power(vex::watt) > 11 || Right3.power(vex::watt) > 11 || Left1.power(vex::watt) > 11 || Left2.power(vex::watt) > 11 || Left3.power(vex::watt) > 11) && clear::power_moitoring < 2){
        short int buffersize = snprintf(nullptr, 0, "%.2f", std::max({Right1.power(vex::watt), Right2.power(vex::watt), Right3.power(vex::watt), Left1.power(vex::watt), Left2.power(vex::watt), Left3.power(vex::watt)}));
        char buffer[buffersize];
        snprintf(buffer, buffersize + 1, "%.2f", std::max({Right1.power(vex::watt), Right2.power(vex::watt), Right3.power(vex::watt), Left1.power(vex::watt), Left2.power(vex::watt), Left3.power(vex::watt)}));
        clear::add("WD1", buffer);
        clear::power_moitoring = 2;
    } 
    else if ((Right1.power(vex::watt) <= 11 || Right2.power(vex::watt) <= 11 || Right3.power(vex::watt) <= 11 || Left1.power(vex::watt) <= 11 || Left2.power(vex::watt) <= 11 || Left3.power(vex::watt) < 11) && clear::power_moitoring > 0){
        short int buffersize = snprintf(nullptr, 0, "%.2f", std::max({Right1.power(vex::watt), Right2.power(vex::watt), Right3.power(vex::watt), Left1.power(vex::watt), Left2.power(vex::watt), Left3.power(vex::watt)}));
        char buffer[buffersize];
        snprintf(buffer, buffersize + 1, "%.2f", std::max({Right1.power(vex::watt), Right2.power(vex::watt), Right3.power(vex::watt), Left1.power(vex::watt), Left2.power(vex::watt), Left3.power(vex::watt)}));
        clear::add("DD1", buffer);
        clear::power_moitoring = 0;
    } 
    
    if (Right1.temperature(vex::percent) == 2 && clear::disconnect_monitoring[0]==false){
        clear::add("ED2", "Right1");
        clear::disconnect_monitoring[0]=true;
    }
    else if (Right1.temperature(vex::percent) != 2  && clear::disconnect_monitoring[0]==true){
        clear::add("DD2", "Right1");
        clear::disconnect_monitoring[0]=false;
    }

    if (Right2.temperature(vex::percent)==2  && clear::disconnect_monitoring[1]==false){
        clear::add("ED2", "Right2");
        clear::disconnect_monitoring[1]=true;
    }
    else if (Right2.temperature(vex::percent) != 2  && clear::disconnect_monitoring[1]==true){
        clear::add("DD2", "Right2");
        clear::disconnect_monitoring[1]=false;
    }

    if (Right3.temperature(vex::percent)==2 && clear::disconnect_monitoring[2]==false){
        clear::add("ED2", "Right3");
        clear::disconnect_monitoring[2]=true;
    }
    else if (Right3.temperature(vex::percent) != 2  && clear::disconnect_monitoring[2]==true){
        clear::add("DD2", "Right3");
        clear::disconnect_monitoring[2]=false;
    }

    if (Left1.temperature(vex::percent)==2 && clear::disconnect_monitoring[3]==false){
        clear::add("ED2", "Left1");
        clear::disconnect_monitoring[3]=true;
    }
    else if (Left1.temperature(vex::percent) != 2  && clear::disconnect_monitoring[3]==true){
        clear::add("DD2", "Left1");
        clear::disconnect_monitoring[3]=false;
    }

    if (Left2.temperature(vex::percent)==2 && clear::disconnect_monitoring[4]==false){
        clear::add("ED2", "Left2");
        clear::disconnect_monitoring[4]=true;
    }
    else if (Left2.temperature(vex::percent) != 2  && clear::disconnect_monitoring[4]==true){
        clear::add("DD2", "Left2");
        clear::disconnect_monitoring[4]=false;
    }

    if (Left3.temperature(vex::percent)==2 && clear::disconnect_monitoring[5]==false){
        clear::add("ED2", "Left3");
        clear::disconnect_monitoring[5]=true;
    }
    else if (Left3.temperature(vex::percent) != 2  && clear::disconnect_monitoring[5]==true){
        clear::add("DD2", "Left3");
        clear::disconnect_monitoring[5]=false;
    }
}

void clear::start(vex::motor Right1, vex::motor Left1, vex::motor Right2 = NULL, vex::motor Left2= NULL, vex::motor Right3 = NULL, vex::motor Left3 = NULL){
    
    clear::add("DS0", "");
    while(true){
        clear:: DrivetarinSixMotor(Right1, Right2, Right3, Left1, Left2, Left3);
        vex::wait(200, vex::msec);
    };
}