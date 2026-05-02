def hybrid_classify(llm_output, ml_output):
    if llm_output["fit_score"] > 0.7:
        return llm_output
    else:
        return {"domain": ml_output, "source": "ml_model"}
