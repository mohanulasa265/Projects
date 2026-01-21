/*******************************************************************************
  PlutoPilot.cpp - lightweight flight-control helper for MagisV2
*******************************************************************************/

#include "PlutoPilot.h"
#include "src/main/API/FC-Data.h"
#include "src/main/API/Scheduler-Timer.h"
#include <stdint.h>
#include <stdio.h>
#include <math.h>

// --- Configuration ---
static const uint32_t PRINT_INTERVAL_MS = 100; // 10 Hz
static const float KP_POS = 1.0f;
static const float STEP_SIZE = 0.05f;
static const uint32_t STEP_PERIOD_MS = 1000;

// --- State ---
static Interval printInterval;
static Interval stepInterval;

static float hoverTargetX = 50.0f;
static float hoverTargetY = 50.0f;
static float hoverTargetZ = 50.0f;

static inline int16_t toCmd16(float v)
{
    long r = lroundf(v);
    if (r > 32767L) r = 32767L;
    if (r < -32768L) r = -32768L;
    return (int16_t)r;
}

// ------------------------------------------------
// FIXED: removed extern "C"
// ------------------------------------------------
void onLoopStart(void)
{
    printInterval.set(PRINT_INTERVAL_MS, true);
    stepInterval.set(STEP_PERIOD_MS, true);

    hoverTargetX = (float) Estimate_Get(Position, X);
    hoverTargetY = (float) Estimate_Get(Position, Y);
    hoverTargetZ = (float) Estimate_Get(Position, Z);

    printf("[PlutoPilot] Initialized (HoverLock X=%.2f Y=%.2f Z=%.2f)\n",
           (double)hoverTargetX, (double)hoverTargetY, (double)hoverTargetZ);
}

// ------------------------------------------------
// FIXED: removed extern "C"
// ------------------------------------------------
void plutoLoop(void)
{
    // --- Read raw sensors ---
    uint32_t accX = Sensor_Get(Accelerometer, X);
    uint32_t accY = Sensor_Get(Accelerometer, Y);
    uint32_t accZ = Sensor_Get(Accelerometer, Z);
    uint32_t accNet = Sensor_Get(Accelerometer, Net_Acc);

    uint32_t gyroX = Sensor_Get(Gyroscope, X);
    uint32_t gyroY = Sensor_Get(Gyroscope, Y);
    uint32_t gyroZ = Sensor_Get(Gyroscope, Z);

    uint32_t press = Sensor_Get(Barometer, Pressure);
    uint32_t temp  = Sensor_Get(Barometer, Temperature);

    int16_t posX = Estimate_Get(Position, X);
    int16_t posY = Estimate_Get(Position, Y);
    int16_t posZ = Estimate_Get(Position, Z);

    int16_t roll  = Estimate_Get(Angle, AG_ROLL);
    int16_t pitch = Estimate_Get(Angle, AG_PITCH);
    int16_t yaw   = Estimate_Get(Angle, AG_YAW);

    // --- step motion ---
    if (stepInterval.check())
    {
        hoverTargetX += STEP_SIZE;
        if (hoverTargetX > 2.0f) hoverTargetX = -2.0f;

        hoverTargetZ += STEP_SIZE * 0.5f;
        if (hoverTargetZ > 3.0f) hoverTargetZ = 0.5f;

        printf("[STEP] New target X=%.2f Y=%.2f Z=%.2f\n",
               (double)hoverTargetX, (double)hoverTargetY, (double)hoverTargetZ);
    }

    // --- simple proportional control ---
    float errX = hoverTargetX - (float)posX;
    float errY = hoverTargetY - (float)posY;
    float errZ = hoverTargetZ - (float)posZ;

    int16_t cmdPitch    = toCmd16(150.0f + KP_POS * errX);
    int16_t cmdRoll     = toCmd16(150.0f + KP_POS * errY);
    int16_t cmdThrottle = toCmd16(150.0f + KP_POS * errZ);

    // --- Print at 10 Hz ---
    if (printInterval.check())
    {
        printf("[DATA] Acc=%lu,%lu,%lu Net=%lu | Gyr=%lu,%lu,%lu\n",
               accX, accY, accZ, accNet, gyroX, gyroY, gyroZ);

        printf("[DATA] Baro P=%lu T=%lu\n", press, temp);

        printf("[DATA] PosEst X=%d Y=%d Z=%d | Ang(r,p,y)=%d,%d,%d\n",
               posX, posY, posZ, roll, pitch, yaw);

        printf("[CMD] Pitch=%d Roll=%d Thr=%d | Err=%.3f %.3f %.3f\n",
               cmdPitch, cmdRoll, cmdThrottle,
               (double)errX, (double)errY, (double)errZ);
    }
}
void plutoRxConfig(){

}
void onLoopFinish(void)
{
    printf("[PlutoPilot] Loop finish\n");
}
