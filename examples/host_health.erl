[
%    {make_install, [{git, "https://github.com/machinezone/mzbench.git"},
%                    {dir, "worker_templates/host_health"}]},
    {pool, [
        {size, 3},
        {worker_type, host_health, python}
    ],
    [
        {my_print, "hello"}
    ]}
].