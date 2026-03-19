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

clear Clear(&Brain);

int main() {
    Clear.add("DS0", "");
    vex::wait(2, vex::seconds);
    Brain.Screen.newLine();
    Clear.add("DS1", "");
    return 0;
}

