from module.mt_text_score import TextScore
import module.utils as utils


def test_score_string():
    # Sentences
    hyp1 = ['It', 'is', 'a', 'guide', 'to', 'action', 'which', 'ensures', 'that', 'the', 'military', 'always', 'obeys',
            'the', 'commands', 'of', 'the', 'party']
    ref1a = ['It', 'is', 'a', 'guide', 'to', 'action', 'that', 'ensures', 'that', 'the', 'military', 'will', 'forever',
             'heed', 'Party', 'commands']
    ref1b = ['It', 'is', 'the', 'guiding', 'principle', 'which', 'guarantees', 'the', 'military', 'forces', 'always',
             'being', 'under', 'the', 'command', 'of', 'the', 'Party']
    ref1c = ['It', 'is', 'the', 'practical', 'guide', 'for', 'the', 'army', 'always', 'to', 'heed', 'the', 'directions',
             'of', 'the', 'party']

    hyp2 = str('he read the book because he was interested in world history').split()
    ref2a = str('he was interested in world history because he read the book').split()

    # Initialize handler for text scores
    text_score = TextScore()
    list_of_references = [[ref1a, ref1b, ref1c], [ref2a]]
    hypotheses = [hyp1, hyp2]

    # BLEU (corpus and sentence average)
    print("")
    gleu_corpus_score = text_score.corpus_score(list_of_references, hypotheses, score_type=utils.BLEU_NAME)
    gleu_sent_average_score = text_score.sentence_average_score(list_of_references, hypotheses, score_type=utils.BLEU_NAME)

    # GLEU (corpus and sentence average)
    print("")
    bleu_corpus_score = text_score.corpus_score(list_of_references, hypotheses, score_type=utils.GOOGLE_BLEU_NAME)
    bleu_sent_average_score = text_score.sentence_average_score(list_of_references, hypotheses, score_type=utils.GOOGLE_BLEU_NAME)


def test_score_file():
    ref_file = utils.project_dir_name()+"assets/test_score_ref.txt"
    hyp_file = utils.project_dir_name() + "assets/test_score_hyp.txt"
    scores_file = utils.project_dir_name() + "assets/test_score.txt"
    scores_meteor_file = utils.project_dir_name() + "assets/test_meteor.txt"

    # Initialize handler for text scores
    text_score = TextScore()
    # BLEU, GLEU, WER, TER
    # text_score.score_multiple_from_file(ref_file, hyp_file, scores_file, score_type="BLEU GLEU", average_prec="corpus sent_average")
    text_score.score_multiple_from_file(ref_file, hyp_file, scores_file,
                                        score_type=utils.BLEU_NAME+utils.GOOGLE_BLEU_NAME+utils.WER_NAME+utils.TER_NAME,
                                        average_prec="corpus, sent_average")

    # METEOR: receives 2 files
    text_score.meteor_score_from_files(ref_file, hyp_file, scores_file=scores_meteor_file)



if __name__ == '__main__':
    # print("\n1. Test score string")
    # test_score_string()

    print("\n2. Test score file")
    test_score_file()



