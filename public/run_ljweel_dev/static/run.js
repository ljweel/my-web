document.addEventListener("DOMContentLoaded", function () {

    const runBtn = document.getElementById("runBtn");
    const codeArea = document.getElementById("code");
    const inputArea = document.getElementById("input");
    const outputArea = document.getElementById("output");
    const debugArea = document.getElementById("debug");;

    
    runBtn.addEventListener("click", async function () {
        const startTime = performance.now();
        const code = codeArea.value;
        const input = inputArea.value;
        
        runBtn.disabled = true;
        try {
            const result = await execute(code, input);

            outputArea.value = result.output;
            debugArea.value = result.debug;
            console.log("debug:" + debug);

        } catch (err) {
            debugArea.value = err.toString();
        }
        finally {
            const endTime = performance.now();
            const duration = endTime - startTime;
            
            const remainingTime = Math.max(0, 1000 - duration);
            await new Promise(r => setTimeout(r, remainingTime));
            runBtn.disabled = false;
        }
    });

});



async function execute(code, input) {
    const baseUrl = "https://run.ljweel.dev";
    const jobStatus = await fetch(`${baseUrl}/execute`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            "language": "python",
            "source_code": code,
            "stdin": input,
        })
    });

    const data = await jobStatus.json();
    const jobId = data.job_id;
    
    
    let jobData;

    while (true) {

        await new Promise(r => setTimeout(r, 500)); // 0.5초 대기

        const statusRes = await fetch(`${baseUrl}/jobs/${jobId}`);
        const data = await statusRes.json();

        if (data.status === "COMPLETED") {
            jobData = data;
            break;
        }

        if (data.status === "FAILED") {
            throw new Error(data.message);
        }
    }
    return {
        output: jobData.result.stdout,
        debug: debugMsg(jobData),
    };
}

function debugMsg(jobData) {
    const { stderr, exit_code, usage_info } = jobData.result;
    const { cpu_time_ms, wall_time_ms } = usage_info;

    return [
        stderr,
        `exit code: ${exit_code ?? "N/A"}`,
        `cpu time: ${cpu_time_ms ?? 0}ms`,
        `wall time: ${wall_time_ms ?? 0}ms`,
    ].join('\n');
}