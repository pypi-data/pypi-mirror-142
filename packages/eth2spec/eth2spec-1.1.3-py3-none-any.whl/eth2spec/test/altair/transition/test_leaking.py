from eth2spec.test.context import fork_transition_test
from eth2spec.test.helpers.constants import PHASE0, ALTAIR
from eth2spec.test.helpers.fork_transition import (
    do_altair_fork,
    transition_until_fork,
    transition_to_next_epoch_and_append_blocks,
)


@fork_transition_test(PHASE0, ALTAIR, fork_epoch=7)
def test_transition_with_leaking_pre_fork(state, fork_epoch, spec, post_spec, pre_tag, post_tag):
    """
    Leaking starts at epoch 6 (MIN_EPOCHS_TO_INACTIVITY_PENALTY + 2).
    The leaking starts before the fork transition in this case.
    """
    transition_until_fork(spec, state, fork_epoch)

    assert spec.is_in_inactivity_leak(state)
    assert spec.get_current_epoch(state) < fork_epoch

    yield "pre", state

    # irregular state transition to handle fork:
    blocks = []
    state, block = do_altair_fork(state, spec, post_spec, fork_epoch)
    blocks.append(post_tag(block))

    # check post transition state
    assert spec.is_in_inactivity_leak(state)

    # continue regular state transition with new spec into next epoch
    transition_to_next_epoch_and_append_blocks(post_spec, state, post_tag, blocks, only_last_block=True)

    yield "blocks", blocks
    yield "post", state


@fork_transition_test(PHASE0, ALTAIR, fork_epoch=6)
def test_transition_with_leaking_at_fork(state, fork_epoch, spec, post_spec, pre_tag, post_tag):
    """
    Leaking starts at epoch 6 (MIN_EPOCHS_TO_INACTIVITY_PENALTY + 2).
    The leaking starts at the fork transition in this case.
    """
    transition_until_fork(spec, state, fork_epoch)

    assert not spec.is_in_inactivity_leak(state)
    assert spec.get_current_epoch(state) < fork_epoch

    yield "pre", state

    # irregular state transition to handle fork:
    blocks = []
    state, block = do_altair_fork(state, spec, post_spec, fork_epoch)
    blocks.append(post_tag(block))

    # check post transition state
    assert spec.is_in_inactivity_leak(state)

    # continue regular state transition with new spec into next epoch
    transition_to_next_epoch_and_append_blocks(post_spec, state, post_tag, blocks, only_last_block=True)

    yield "blocks", blocks
    yield "post", state
