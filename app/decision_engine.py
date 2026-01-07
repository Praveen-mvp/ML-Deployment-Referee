def compare_deployment(inputs):
    hardware = inputs["hardware"]
    deployment = inputs["deployment"]
    latency = inputs["latency"]
    cost = inputs["cost"]

    options = []

    # PyTorch FP32
    options.append({
        "name": "PyTorch FP32",
        "pros": [
            "Highest accuracy",
            "No model conversion",
            "Easy debugging"
        ],
        "cons": [
            "High memory usage",
            "Slow inference",
            "Not cost efficient"
        ],
        "best_for": "Research and prototyping"
    })

    # PyTorch INT8
    options.append({
        "name": "PyTorch INT8",
        "pros": [
            "Lower latency on CPU",
            "Reduced memory footprint",
            "Cost efficient"
        ],
        "cons": [
            "Possible accuracy drop",
            "Calibration required"
        ],
        "best_for": "Edge and CPU deployments"
    })

    # ONNX Runtime
    options.append({
        "name": "ONNX Runtime",
        "pros": [
            "Cross-platform",
            "Stable production runtime",
            "Multiple hardware backends"
        ],
        "cons": [
            "Model conversion overhead",
            "Harder debugging"
        ],
        "best_for": "Production deployments"
    })

    # TensorRT
    if hardware == "GPU":
        options.append({
            "name": "TensorRT",
            "pros": [
                "Lowest latency",
                "Best GPU throughput",
                "FP16 and INT8 support"
            ],
            "cons": [
                "NVIDIA GPU only",
                "Complex setup"
            ],
            "best_for": "High performance GPU inference"
        })

    recommendation = decide_best_option(hardware, deployment, latency, cost)

    return {
        "inputs": inputs,
        "options": options,
        "recommended": recommendation
    }


def decide_best_option(hardware, deployment, latency, cost):
    if hardware == "GPU" and latency == "high":
        return "TensorRT"

    if hardware == "CPU" and deployment == "edge":
        return "PyTorch INT8"

    if deployment == "cloud" and cost == "high":
        return "ONNX Runtime"

    return "PyTorch FP32"

