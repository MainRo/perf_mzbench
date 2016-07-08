[
%    {make_install, [{git, "https://github.com/machinezone/mzbench.git"},
%                    {git, "https://github.com/MainRo/perf_mzbench.git"}]},
    {pool, [
        {size, 3},
        {worker_type, perf_worker, python}
    ],
        [{loop,
            [{time, {30, sec}},
                {rate, {12, rpm}}],
           [{get_perf_metrics, "localhost", 4242}]}]
    }
].
