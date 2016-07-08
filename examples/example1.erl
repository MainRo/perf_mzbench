[
%    {make_install, [{git, "https://github.com/machinezone/mzbench.git"},
%                    {dir, "worker_templates/perf_mzbench"}]},
    {pool, [
        {size, 3},
        {worker_type, perf_worker, python}
    ],
    [
        {start_monitoring},
        {wait, {30, sec}},
        {stop_monitoring}
    ]}
].
