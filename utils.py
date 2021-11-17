import json

def write_st_object(obj):
    """
    Object spec:
    {
      "status": "started" | "poll" | "ready",
      "st_inputs": {} | None,
      "first_phase_output": {} | None
    }
    """
    with open("streamlit-sync.json", "w") as f:
        json.dump(obj, f)
        
def read_st_object():
    with open("streamlit-sync.json", "r") as f:
        return json.load(f)
