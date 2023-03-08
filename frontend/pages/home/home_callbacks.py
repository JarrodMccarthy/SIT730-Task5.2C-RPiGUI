from dash import Input, Output
from app import app

import RPi.GPIO as GPIO

def switch_led(pin: int, state: bool) -> bool:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    if state: 
        GPIO.output(pin, GPIO.HIGH)
    else:
        GPIO.output(pin, GPIO.LOW)    
    return state


@app.callback(
    Output('overview-div', 'children'),
    [Input('green', 'on'), Input('amber', 'on'), Input('red', 'on')],
)
def update_output(green_state: bool, amber_state: bool, red_state: bool):
    green_pin = 4
    amber_pin = 3
    red_pin = 2
    green_feedback = switch_led(green_pin, green_state)
    amber_feedback = switch_led(amber_pin, amber_state)
    red_feedback = switch_led(red_pin, red_state)
    return f'The green button is {green_feedback}, The amber button is {amber_feedback}, The red button is {red_feedback}'