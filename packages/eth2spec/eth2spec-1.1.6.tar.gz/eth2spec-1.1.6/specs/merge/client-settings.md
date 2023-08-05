<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [The Merge -- Client Settings](#the-merge----client-settings)
    - [Override terminal total difficulty](#override-terminal-total-difficulty)
    - [Override terminal block hash](#override-terminal-block-hash)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# The Merge -- Client Settings

**Notice**: This document is a work-in-progress for researchers and implementers.

This document specifies configurable settings that clients must implement for the Merge.

### Override terminal total difficulty

To coordinate manual overrides to [`TERMINAL_TOTAL_DIFFICULTY`](./beacon-chain.md#Transition-settings) parameter, clients must provide `--terminal-total-difficulty-override` as a configurable setting. The value provided by this setting must take precedence over pre-configured `TERMINAL_TOTAL_DIFFICULTY` parameter. Clients should accept the setting as a decimal value (i.e., *not* hexadecimal).

Except under exceptional scenarios, this setting is not expected to be used. Sufficient warning to the user about this exceptional configurable setting should be provided.

### Override terminal block hash

To allow for transition coordination around a specific PoW block, clients must also provide `--terminal-block-hash-override` and `--terminal-block-hash-epoch-override` as configurable settings.
* The value provided by `--terminal-block-hash-override` takes precedence over the pre-configured `TERMINAL_BLOCK_HASH` parameter.
* The value provided by `--terminal-block-hash-epoch-override` takes precedence over the pre-configured `TERMINAL_BLOCK_HASH_ACTIVATION_EPOCH` parameter.

Except under exceptional scenarios, these settings are not expected to be used. Sufficient warning to the user about this exceptional configurable setting should be provided.
