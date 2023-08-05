def benchmark_single_jr_circuit(n_runs=10):
    """This is a simple benchmark function that instantiates a basic JR circuit and compiles it.

    Parameters
    ----------
    n_runs
        number of runs to execute benchmark for averaging
    """

    import time
    from pyrates.frontend.template.circuit import CircuitTemplate
    from pyrates.frontend import clear_frontend_caches
    import numpy as np

    path = "model_templates.jansen_rit.circuit.JansenRitCircuit"

    timer_dict = dict(template_load=[],
                      template_apply=[],
                      # circuit_compile=[]
                      )

    for i in range(n_runs):
        # time template loading
        tic = time.perf_counter()
        template = CircuitTemplate.from_yaml(path)
        toc = time.perf_counter()
        timer_dict["template_load"].append(toc - tic)

        # time template application to circuit IR
        tic = time.perf_counter()
        circuit = template.apply()
        toc = time.perf_counter()
        timer_dict["template_apply"].append(toc - tic)

        # time circuit compilation (probably irrelevant in this case
        # tic = time.perf_counter()
        # circuit.compile()
        # toc = time.perf_counter()
        # timer_dict["circuit_compile"].append(toc-tic)

        clear_frontend_caches()

    print("Benchmark results:")
    for key, times in timer_dict.items():
        median = np.median(times)

        print(f"{key}: {median:.4f}s")


if __name__ == "__main__":
    benchmark_single_jr_circuit(10)
