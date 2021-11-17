import time
import json

import orchest

import utils

action = orchest.get_step_param("action")

if action == "start":
    utils.write_st_object({
        "status": "started"
    })
elif action == "poll":
    utils.write_st_object({
        "status": "poll",
        "first_phase_output": orchest.get_inputs()["first_phase_output"]
    })
    
    while True:
        st_obj = utils.read_st_object()
        
        if st_obj["status"] != "ready":
            print(".", end="", flush=True)
            time.sleep(1)
        else:
            print("Received input, continuing")
            break
    
    print("Passing:")
    print(st_obj["st_inputs"])
    
    orchest.output(st_obj["st_inputs"], name="st_inputs")
