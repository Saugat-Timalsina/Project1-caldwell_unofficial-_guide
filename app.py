import gradio as gr
from query import ask


def handle_query(question):
    if not question.strip():
        return "Please enter a question.", ""

    result = ask(question)

    answer = result["answer"]
    sources = "\n".join(f"- {source}" for source in result["sources"])

    return answer, sources


with gr.Blocks(title="Caldwell Unofficial CS Guide") as demo:
    gr.Markdown("# The Unofficial Guide to Caldwell CS")
    gr.Markdown(
        "Ask questions about Caldwell University CS professors, CS courses, difficulty, feedback, workload, and official CS pathways."
    )

    question = gr.Textbox(
        label="Your question",
        placeholder="Example: Which professor gives good feedback?",
    )

    ask_button = gr.Button("Ask")

    answer = gr.Textbox(label="Answer", lines=8)
    sources = gr.Textbox(label="Retrieved sources", lines=5)

    ask_button.click(handle_query, inputs=question, outputs=[answer, sources])
    question.submit(handle_query, inputs=question, outputs=[answer, sources])


if __name__ == "__main__":
    demo.launch()