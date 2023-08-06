import torch
from torch import nn
import torch.nn.functional as F
from typing import Dict


def make_tokens(input_text):
    r"""Computes all unique characters in the `input_text`.

    Parameters
    ----------
    input_text : str
        Input text for RNN training. Should be simple plain text file.

    Returns
    -------
    tokens : list of str
        List with all unique tokens.
    """
    # TODO: implement make_tokens
    # Your final implementation shouldn't have any loops
    raise NotImplementedError('Not implemented!')


def make_token_to_id(tokens):
    r"""Creates mapping between tokens and its int identifiers.

    Parameters
    ----------
    tokens : list of str
        List with all unique tokens.

    Returns
    -------
    token_to_id : dict of str
        Tokens to its identifier (index in tokens list).
    """
    # TODO: make_token_to_id
    raise NotImplementedError('Not implemented!')


class CharRNNCell(nn.Module):
    r"""Implement vanilla rnn-cell as torch module.

    Attributes
    ----------
    num_units : ...
        ...
    embedding : ...
        ...
    rnn_update : ...
        ...
    rnn_to_logits : ...
        ...
    """
    def __init__(self, num_tokens, embedding_size=16, rnn_num_units=64):
        super(self.__class__, self).__init__()
        self.num_units = rnn_num_units

        self.embedding = nn.Embedding(num_tokens, embedding_size)
        self.rnn_update = nn.Linear(
            embedding_size + rnn_num_units,
            rnn_num_units,
        )
        self.rnn_to_logits = nn.Linear(rnn_num_units, num_tokens)

    def forward(self, x, h_prev):
        r"""Compute h_next(x, h_prev) and log(P(x_next | h_next)).
        We'll call it repeatedly to produce the whole sequence.

        Parameters
        ----------
        x : LongTensor, shape(batch_size)
            Batch of character ids.
        h_prev : FloatTensor, shape(batch, rnn_num_units)
            Previous rnn hidden states.

        Returns
        -------

        """
        # get vector embedding of x
        x_emb = self.embedding(x)

        # TODO: compute next hidden state using self.rnn_update
        # hint: use torch.cat(..., dim=...) for concatenation
        # h_next = ...
        raise NotImplementedError('Not implemented!')

        h_next = torch.tanh(h_next)

        assert h_next.size() == h_prev.size()

        # TODO: compute logits for next character probs
        # logits = ...
        raise NotImplementedError('Not implemented!')

        return h_next, F.log_softmax(logits, -1)

    def initial_state(self, batch_size):
        r"""Returns rnn state before it processes first input (aka h0) """
        return torch.zeros(batch_size, self.num_units)


def train(lines):
    r"""Implement RNN training loop.

    Parameters
    ----------
    lines : list of str
        Lines of input text.
    """
    for i in range(1000):
        raise NotImplementedError('Not implemented!')
        # batch_ix = to_matrix(sample(lines, 32), max_len=MAX_LENGTH)
        # batch_ix = torch.tensor(batch_ix, dtype=torch.int64)
        #
        # # TODO: implement train loop
        #
        # logp_seq = rnn_loop(char_rnn, batch_ix)
        #
        # # TODO: compute loss
        #
        #
        # # loss = ...
        #
        # # TODO: backprop
        #
        # history.append(loss.data.numpy())
        # if (i+1)%100==0:
        #     clear_output(True)
        #     plt.plot(history,label='loss')
        #     plt.legend()
        #     plt.show()
