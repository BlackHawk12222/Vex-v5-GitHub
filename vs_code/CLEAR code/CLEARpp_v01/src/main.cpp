/*----------------------------------------------------------------------------*/
/*                                                                            */
/*    Module:       main.cpp                                                  */
/*    Author:       MicaS                                                     */
/*    Created:      3/18/2026, 2:52:13 PM                                     */
/*    Description:  V5 project                                                */
/*                                                                            */
/*----------------------------------------------------------------------------*/

#include "vex.h"
#include "CLEAR.hpp"

vex::brain Brain;
// A global instance of vex::brain used for printing to the V5 brain screen

// define your global instances of motors and other devices here
vex::motor Right1 = vex::motor(vex::PORT1, vex::ratio6_1);
vex::motor Right2 = vex::motor(vex::PORT2, vex::ratio6_1);
vex::motor Right3 = vex::motor(vex::PORT3, vex::ratio6_1);
vex::motor Left1 = vex::motor(vex::PORT4, vex::ratio6_1, true);
vex::motor Left2 = vex::motor(vex::PORT5, vex::ratio6_1, true);
vex::motor Left3 = vex::motor(vex::PORT6, vex::ratio6_1, true);

clear Clear(&Brain);

int main() {
    Brain.Screen.setFont(vex::mono12);
    Clear.start(Right1, Left1, Right2, Left2, Right3, Left3);
    Brain.Screen.newLine();
    Clear.add("DS1", "");
    return 0;
}

