from ev3dev.auto import OUTPUT_A, Motor, OUTPUT_B
import time

ma = Motor(OUTPUT_A)
ma.run_forever(duty_cycle_sp = 100)
time.sleep(1)
ma.stop()

time.sleep(5)

mb = Motor(OUTPUT_B)
mb.runforever(duty_cycle_sp = 100)
time.sleep(1)
mb.stop()
