# Lint as: python3
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Constants used in TensorFlow Model Analysis."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Mode for multiple model analysis runs
UNKNOWN_EVAL_MODE = 'unknown_eval_mode'
MODEL_CENTRIC_MODE = 'model_centric_mode'
DATA_CENTRIC_MODE = 'data_centric_mode'

# Types of placeholders
PLACEHOLDER = 'placeholder'
SPARSE_PLACEHOLDER = 'sparse_placeholder'

# Types of models
TF_ESTIMATOR = 'tf_estimator'
TF_KERAS = 'tf_keras'
TF_GENERIC = 'tf_generic'
TF_LITE = 'tf_lite'
VALID_MODEL_TYPES = ('', TF_GENERIC, TF_ESTIMATOR, TF_KERAS, TF_LITE)

# LINT.IfChange
METRICS_NAMESPACE = 'tfx.ModelAnalysis'
# LINT.ThenChange(../../../learning/fairness/infra/plx/scripts/tfma_metrics_computed_tracker_macros.sql)

# Keys for Extracts dictionary (keys starting with _ will not be materialized).

# Input key. Could be a serialised tf.train.Example, a CSV row, JSON data, etc
# depending on what the EvalInputReceiver was configured to accept as input.
INPUT_KEY = 'input'

# This holds an Arrow RecordBatch representing a batch of examples.
ARROW_RECORD_BATCH_KEY = 'arrow_record_batch'

# Batched input key. Could be a batch of serialized tf.train.Example, CSV
# row, JSON data etc.
BATCHED_INPUT_KEY = 'batched_input'

# Batched features key.
BATCHED_FEATURES_KEY = 'batched_features'

# Batched labels key.
BATCHED_LABELS_KEY = 'batched_labels'

# Batched predictions key.
BATCHED_PREDICTIONS_KEY = 'batched_predictions'

# Batched example weights key.
BATCHED_EXAMPLE_WEIGHTS_KEY = 'batched_example_weights'

# Features, predictions, and labels key.
FEATURES_PREDICTIONS_LABELS_KEY = '_fpl'
# Contains SliceKeyTypes that are used to fanout and aggregate.
SLICE_KEY_TYPES_KEY = '_slice_key_types'
# Human-readable slice strings that are written to the diagnostic table for
# analysis.
SLICE_KEYS_KEY = 'slice_keys'
# Features key.
FEATURES_KEY = 'features'
# Labels key.
LABELS_KEY = 'labels'
# Predictions key.
PREDICTIONS_KEY = 'predictions'
# Example weights key.
EXAMPLE_WEIGHTS_KEY = 'example_weights'
# Attributions key.
ATTRIBUTIONS_KEY = 'attributions'

# Keys used for standard attribution scores
BASELINE_SCORE_KEY = 'baseline_score'
EXAMPLE_SCORE_KEY = 'example_score'

# Keys for Evaluation/Validation dictionaries

# Metrics output key.
METRICS_KEY = 'metrics'
# Plots output key.
PLOTS_KEY = 'plots'

# Validations key.
VALIDATIONS_KEY = 'validations'
# Analysis output key.
ANALYSIS_KEY = 'analysis'

# Keys for validation alternatives
BASELINE_KEY = 'baseline'
CANDIDATE_KEY = 'candidate'

MATERIALIZE_COLUMNS = 'materialize'
