from dash import Input, Output
from app import app

# import RPi.GPIO

# def switch_led(pin: int, state: bool) -> bool:
#     GPIO.setmode(GPIO.BCM)
#     GPIO.setup(pin)
#     if state: 
#         GPIO.output(pin, GPIO.HIGH)
#     else:
#         GPIO.output(pin, GPIO.LOW)    
#     return state


@app.callback(
    Output('overview-div', 'children'),
    [Input('green', 'on'), Input('amber', 'on'), Input('red', 'on')],
)
def update_output(green, amber, red):
    print(f'The green button is {green}, The amber button is {amber}, The red button is {red}')
    return f'The green button is {green}, The amber button is {amber}, The red button is {red}'