import torch
from transformers import LongformerTokenizer, LongformerForQuestionAnswering


def question_over_context(context, question, model_id="valhalla/longformer-base-4096-finetuned-squadv1"):
    tokenizer = LongformerTokenizer.from_pretrained(
        model_id
    )
    model = LongformerForQuestionAnswering.from_pretrained(
        model_id
    )

    encoding = tokenizer.encode_plus(question, context, return_tensors="pt")
    input_ids = encoding["input_ids"]

    # default is local attention everywhere
    # the forward method will automatically set global attention on question tokens
    attention_mask = encoding["attention_mask"]

    outputs = model(input_ids, attention_mask=attention_mask)
    start_scores = outputs["start_logits"]
    end_scores = outputs["end_logits"]
    all_tokens = tokenizer.convert_ids_to_tokens(input_ids[0].tolist())

    answer_tokens = all_tokens[torch.argmax(start_scores):torch.argmax(end_scores) + 1]
    answer = tokenizer.decode(tokenizer.convert_tokens_to_ids(answer_tokens))
    return answer

if __name__ == "__main__":
    pass
