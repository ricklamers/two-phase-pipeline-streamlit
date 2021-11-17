# Two phase pipeline + Streamlit

This is an example project that demonstrates how to create a pipeline that consists of **two phases of execution**.

In between the two phases the computations of the first phase influence what should happen in the second phase. It allows for a **human in the loop** scenario.

Override the `show_first_phase_outputs` and `collect_user_inputs` functions in `streamlit.py` to change how the information from the first phase is presented to the user and what information is collected from the user as input for the second phase.

`work.py` and `more-work.py` are basic placeholders for the first and second phase of the pipeline. These can be replaced by an arbitrary number of pipeline steps. As long as the pipeline starts with the `[Two phase] Start` step and the first phase ends with `[Two phase] poll`. It's important that the step prior to `[Two phase] poll` outputs an output named `first_phase_output` (see `work.py`).

![Two phase pipeline visualization](https://pviz.orchest.io/?pipeline=https://github.com/ricklamers/two-phase-pipeline-streamlit/blob/main/main.orchest)
