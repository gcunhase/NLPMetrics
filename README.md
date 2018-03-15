### About

* Natural Language Processing Metrics for Performance

* Average precision:
    * *Macro*: average of sentence scores
    * *Micro*: corpus (sums numerators and denominators for each hypothesis-reference(s) pairs before division)

### Machine Translation
1. BLEU (Bilingual Evaluation Understudy) score limitation (Papineni 2002): designed to be a corpus measure, so
            it has undesirable properties when used for single sentences. 'Measures how many words overlap in a given
             translation when compared to a reference translation, giving higher scores to sequential words.'
            See [paper](https://www.aclweb.org/anthology/P02-1040.pdf)
2. GLEU (Google-BLEU) score (Wu et al. 2016): minimum of BLEU recall and precision applied to 1, 2, 3 and 4grams
            Recall: (number of matching n-grams) / (number of total n-grams in the target)
            Precision: (number of matching n-grams) / (number of total n-grams in generated sequence)
3. Word error rate (WER)
4. Skip-gram: similar to word embedding
5. METEOR (Metric for Evaluation of Translation with Explicit ORdering):
6. Translation Edit Rate (TER)
7. char-TER
8. General Text Matcher (GTM)


### Summarization
1. ROUGE (Recall-Oriented Understudy for Gisting Evaluation):