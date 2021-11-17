import time
import os

import streamlit as st

import utils


# User defined functions
def show_first_phase_outputs(first_phase_output):
    """
        This function displays the outputs of the 
        first phase of the pipeline to help the user 
        choose the right inputs for the second phase
        of the pipeline.
        
        Change it to your liking.
    """
    st.write(first_phase_output)


def collect_user_inputs():
    """
        This function collects the required inputs from the user to execute
        the second phase of the pipeline.
        
        Change it to your liking.
    """
    name = st.text_input('Name', '')
    return {"name": name }
# End of user defined functions


def show_collection_machine():
    """
        Don't change this function, it marshals the
        first_phase_output and st_inputs.
    """
    if st.button('Refresh'):
        pass

    # Wait until phase one is complete
    st_obj = utils.read_st_object()

    if st_obj["status"] == "poll":
        show_first_phase_outputs(st_obj["first_phase_output"])

        st_inputs = collect_user_inputs()

        if st.button('Submit'):
            utils.write_st_object({
                "status": "ready",
                "st_inputs": st_inputs
            })

            st.subheader('Submitted input! Execution continuing. Check the pipeline...')
    elif st_obj["status"] == "ready":
        st.write("Submitted input to second phase:")
        st.write(st_obj["st_inputs"])
    else:
        st.write("First phase is still executing")


show_collection_machine()