# regole2_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1
from compiled_krb import regole2_plans

def meteo(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('fatti', 'tempo', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.meteo: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def nucleo_utente_fam(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'tipo_nucleo', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.nucleo_utente_fam: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'Famiglia'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def nucleo_utente_amici(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'tipo_nucleo', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.nucleo_utente_amici: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'Amici'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def nucleo_utente_coppia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'tipo_nucleo', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.nucleo_utente_coppia: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'Coppia'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def nucleo_utente_solo(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'tipo_nucleo', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.nucleo_utente_solo: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'Solo'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def nucleo_utente_affari(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'tipo_nucleo', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.nucleo_utente_affari: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'Affari'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def piace_natura(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'natura', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.piace_natura: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'piace_natura'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_piace_natura(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'natura', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.no_piace_natura: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'no_piace_natura'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def scegli_loc_blu(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'mare_o_collina', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.scegli_loc_blu: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'Blu'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def scegli_loc_verde(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'mare_o_collina', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.scegli_loc_verde: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'Verde'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def piace_arte(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'arte', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.piace_arte: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'piace_arte'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_piace_arte(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'arte', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.no_piace_arte: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'no_piace_arte'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_1_bello_Famiglia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'natura', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_1_bello_Famiglia: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_1_brutto_Famiglia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'storia', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_1_brutto_Famiglia: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_2_bello_Famiglia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'verde_blu', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_2_bello_Famiglia: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_2_brutto_Famiglia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'artista', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_2_brutto_Famiglia: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domada_gen_2_not_bello_Famiglia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'artista', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domada_gen_2_not_bello_Famiglia: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domada_gen_2_not_brutto_Famiglia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'shopping', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domada_gen_2_not_brutto_Famiglia: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_1_bello_Coppia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'natura', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_1_bello_Coppia: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_1_brutto_Coppia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'storia', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_1_brutto_Coppia: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_2_bello_Coppia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'verde_blu', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_2_bello_Coppia: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_2_brutto_Coppia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'artista', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_2_brutto_Coppia: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domada_gen_2_not_bello_Coppia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'citta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domada_gen_2_not_bello_Coppia: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domada_gen_2_not_brutto_Coppia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'shopping', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domada_gen_2_not_brutto_Coppia: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_1_bello_Solo(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'natura', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_1_bello_Solo: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_1_brutto_Solo(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'storia', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_1_brutto_Solo: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_2_bello_Solo(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'verde_blu', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_2_bello_Solo: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_2_brutto_Solo(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'artista', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_2_brutto_Solo: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domada_gen_2_not_bello_Solo(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'citta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domada_gen_2_not_bello_Solo: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domada_gen_2_not_brutto_Solo(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'shopping', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domada_gen_2_not_brutto_Solo: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_1_bello_Affari(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'tempo_occupato', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_1_bello_Affari: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_1_brutto_Affari(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'tempo_occupato', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_1_brutto_Affari: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domada_gen_2_not_bello_Affari(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'natura', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domada_gen_2_not_bello_Affari: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domada_gen_2_not_brutto_Affari(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'storia', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domada_gen_2_not_brutto_Affari: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_1_bello_Famiglia_a(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'natura', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_1_bello_Famiglia_a: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_1_brutto_Famiglia_a(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'bruttotempo', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_1_brutto_Famiglia_a: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_2_bello_Famiglia_a(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'sport', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_2_bello_Famiglia_a: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_2_brutto_Famiglia_a(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'natura', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_2_brutto_Famiglia_a: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domada_gen_2_not_bello_Famiglia_a(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'storia', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domada_gen_2_not_bello_Famiglia_a: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domada_gen_2_not_brutto_Famiglia_a(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'storia', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domada_gen_2_not_brutto_Famiglia_a: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_1_bello_Coppia_a(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'natura', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_1_bello_Coppia_a: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_1_brutto_Coppia_a(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'bruttotempo', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_1_brutto_Coppia_a: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_2_bello_Coppia_a(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'sport', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_2_bello_Coppia_a: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_2_brutto_Coppia_a(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'natura', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_2_brutto_Coppia_a: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domada_gen_2_not_bello_Coppia_a(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'storia', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domada_gen_2_not_bello_Coppia_a: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domada_gen_2_not_brutto_Coppia_a(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'storia', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domada_gen_2_not_brutto_Coppia_a: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def brutto_tempo(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'brutto_tempo', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.brutto_tempo: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'piace_bagnarsi'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_brutto_tempo(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'brutto_tempo', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.no_brutto_tempo: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'no_piace_bagnarsi'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def tempo_libero(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'tempo', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.tempo_libero: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'sempre_occupato'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_tempo_libero(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'tempo', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.no_tempo_libero: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'no_sempre_occupato'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def bere_qualcosa(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'bere', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.bere_qualcosa: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'bere'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_bere_qualcosa(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'bere', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.no_bere_qualcosa: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'no_bere'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def piace_storia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'storia', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.piace_storia: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'piace_storia'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_piace_storia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'storia', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.no_piace_storia: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'no_piace_storia'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def piace_shopping(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'shopping', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.piace_shopping: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'piace_shopping'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_piace_shopping(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'shopping', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.no_piace_shopping: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'no_piace_shopping'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def scelta_tipo_vacanza_relax(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'tipo_vacanza', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.scelta_tipo_vacanza_relax: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'Rilassante'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def scelta_tipo_vacanza_jamesbond(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'tipo_vacanza', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.scelta_tipo_vacanza_jamesbond: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'Avventuriera'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def piace_sport(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'sport', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.piace_sport: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'piace_sport'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_piace_sport(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'sport', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.no_piace_sport: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'no_piace_sport'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def scelta_tipo_vacanza_divertimento(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'tipo_vacanza', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is not None, \
              "regole2.scelta_tipo_vacanza_divertimento: expected plan from when clause 1"
            mark1 = context.mark(True)
            if not rule.pattern(1).match_data(context, context, x_1):
              raise AssertionError("regole2.scelta_tipo_vacanza_divertimento: plan match to $plan#1 failed in when clause 1")
            context.end_save_all_undo()
            rule.rule_base.num_bc_rule_successes += 1
            yield context
            context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def fine(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('fatti', 'tipologia', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),
                           rule.pattern(4),
                           rule.pattern(5),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.fine: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cosa_fare(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'meteo', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.cosa_fare: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'nucleo', context,
                              (rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "regole2.cosa_fare: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'tipologia_vacanza', context,
                                  (rule.pattern(4),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "regole2.cosa_fare: got unexpected plan from when clause 3"
                    with engine.prove(rule.rule_base.root_name, 'domanda1', context,
                                      (rule.pattern(4),
                                       rule.pattern(2),
                                       rule.pattern(3),
                                       rule.pattern(5),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "regole2.cosa_fare: got unexpected plan from when clause 4"
                        with engine.prove(rule.rule_base.root_name, 'domanda2', context,
                                          (rule.pattern(4),
                                           rule.pattern(2),
                                           rule.pattern(3),
                                           rule.pattern(5),
                                           rule.pattern(6),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "regole2.cosa_fare: got unexpected plan from when clause 5"
                            with engine.prove(rule.rule_base.root_name, 'conclusione', context,
                                              (rule.pattern(4),
                                               rule.pattern(2),
                                               rule.pattern(3),
                                               rule.pattern(5),
                                               rule.pattern(6),
                                               rule.pattern(7),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "regole2.cosa_fare: got unexpected plan from when clause 6"
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def mangiare(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'mangiare_bere', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.mangiare: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'mangiare'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def bere(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'mangiare_bere', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.bere: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'bere'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def giochi(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'giochi', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.giochi: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'piace_giochi'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_giochi(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'giochi', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.no_giochi: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'no_piace_giochi'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def citta(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'citta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.citta: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'piace_citta'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_citta(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'citta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.no_citta: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'no_piace_citta'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def tipico(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'tipico', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.tipico: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'piace_tipico'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_tipico(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('user_questions', 'tipico', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.no_tipico: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                   'no_piace_tipico'):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_1_amici_rilassante_brutto_tempo(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'tipico', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_1_amici_rilassante_brutto_tempo: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_1_amici_rilassante_bel_tempo(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'natura', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_1_amici_rilassante_bel_tempo: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_2_amici_rilassante_brutto_tempo(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'mangiare', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_2_amici_rilassante_brutto_tempo: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_2_amici_rilassante_brutto_tempo_not(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'giochi', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_2_amici_rilassante_brutto_tempo_not: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_2_amici_rilassante_bel_tempo(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'verde_blu', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_2_amici_rilassante_bel_tempo: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_2_amici_rilassante_bel_tempo_not(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'citta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_2_amici_rilassante_bel_tempo_not: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def domanda_gen_2_bello_Affari(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'bere', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regole2.domanda_gen_2_bello_Affari: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('regole2')
  
  bc_rule.bc_rule('meteo', This_rule_base, 'meteo',
                  meteo, None,
                  (contexts.variable('prev'),
                   contexts.variable('temp'),
                   contexts.variable('risp'),),
                  (),
                  (contexts.variable('prev'),
                   contexts.variable('temp'),
                   contexts.variable('risp'),))
  
  bc_rule.bc_rule('nucleo_utente_fam', This_rule_base, 'nucleo',
                  nucleo_utente_fam, None,
                  (contexts.variable('nucleo_fam'),),
                  (),
                  (pattern.pattern_literal('Famiglia'),
                   contexts.variable('nucleo_fam'),))
  
  bc_rule.bc_rule('nucleo_utente_amici', This_rule_base, 'nucleo',
                  nucleo_utente_amici, None,
                  (contexts.variable('nucleo_fam'),),
                  (),
                  (pattern.pattern_literal('Amici'),
                   contexts.variable('nucleo_fam'),))
  
  bc_rule.bc_rule('nucleo_utente_coppia', This_rule_base, 'nucleo',
                  nucleo_utente_coppia, None,
                  (contexts.variable('nucleo_fam'),),
                  (),
                  (pattern.pattern_literal('Coppia'),
                   contexts.variable('nucleo_fam'),))
  
  bc_rule.bc_rule('nucleo_utente_solo', This_rule_base, 'nucleo',
                  nucleo_utente_solo, None,
                  (contexts.variable('nucleo_fam'),),
                  (),
                  (pattern.pattern_literal('Solo'),
                   contexts.variable('nucleo_fam'),))
  
  bc_rule.bc_rule('nucleo_utente_affari', This_rule_base, 'nucleo',
                  nucleo_utente_affari, None,
                  (contexts.variable('nucleo_fam'),),
                  (),
                  (pattern.pattern_literal('Affari'),
                   contexts.variable('nucleo_fam'),))
  
  bc_rule.bc_rule('piace_natura', This_rule_base, 'natura',
                  piace_natura, None,
                  (contexts.variable('natura'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('natura'),))
  
  bc_rule.bc_rule('no_piace_natura', This_rule_base, 'natura',
                  no_piace_natura, None,
                  (contexts.variable('natura'),),
                  (),
                  (pattern.pattern_literal(False),
                   contexts.variable('natura'),))
  
  bc_rule.bc_rule('scegli_loc_blu', This_rule_base, 'verde_blu',
                  scegli_loc_blu, None,
                  (contexts.variable('paesaggio'),),
                  (),
                  (pattern.pattern_literal('Blu'),
                   contexts.variable('paesaggio'),))
  
  bc_rule.bc_rule('scegli_loc_verde', This_rule_base, 'verde_blu',
                  scegli_loc_verde, None,
                  (contexts.variable('paesaggio'),),
                  (),
                  (pattern.pattern_literal('Verde'),
                   contexts.variable('paesaggio'),))
  
  bc_rule.bc_rule('piace_arte', This_rule_base, 'artista',
                  piace_arte, None,
                  (contexts.variable('arte'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('arte'),))
  
  bc_rule.bc_rule('no_piace_arte', This_rule_base, 'artista',
                  no_piace_arte, None,
                  (contexts.variable('arte'),),
                  (),
                  (pattern.pattern_literal(False),
                   contexts.variable('arte'),))
  
  bc_rule.bc_rule('domanda_gen_1_bello_Famiglia', This_rule_base, 'domanda1',
                  domanda_gen_1_bello_Famiglia, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('bel_tempo'),
                   pattern.pattern_literal('Famiglia'),
                   contexts.variable('answer1'),),
                  (),
                  (contexts.variable('answer1'),))
  
  bc_rule.bc_rule('domanda_gen_1_brutto_Famiglia', This_rule_base, 'domanda1',
                  domanda_gen_1_brutto_Famiglia, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('brutto_tempo'),
                   pattern.pattern_literal('Famiglia'),
                   contexts.variable('answer1'),),
                  (),
                  (contexts.variable('answer1'),))
  
  bc_rule.bc_rule('domanda_gen_2_bello_Famiglia', This_rule_base, 'domanda2',
                  domanda_gen_2_bello_Famiglia, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('bel_tempo'),
                   pattern.pattern_literal('Famiglia'),
                   pattern.pattern_literal('piace_natura'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))
  
  bc_rule.bc_rule('domanda_gen_2_brutto_Famiglia', This_rule_base, 'domanda2',
                  domanda_gen_2_brutto_Famiglia, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('brutto_tempo'),
                   pattern.pattern_literal('Famiglia'),
                   pattern.pattern_literal('piace_storia'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))
  
  bc_rule.bc_rule('domada_gen_2_not_bello_Famiglia', This_rule_base, 'domanda2',
                  domada_gen_2_not_bello_Famiglia, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('bel_tempo'),
                   pattern.pattern_literal('Famiglia'),
                   pattern.pattern_literal('no_piace_natura'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))
  
  bc_rule.bc_rule('domada_gen_2_not_brutto_Famiglia', This_rule_base, 'domanda2',
                  domada_gen_2_not_brutto_Famiglia, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('brutto_tempo'),
                   pattern.pattern_literal('Famiglia'),
                   pattern.pattern_literal('no_piace_storia'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))
  
  bc_rule.bc_rule('domanda_gen_1_bello_Coppia', This_rule_base, 'domanda1',
                  domanda_gen_1_bello_Coppia, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('bel_tempo'),
                   pattern.pattern_literal('Coppia'),
                   contexts.variable('answer1'),),
                  (),
                  (contexts.variable('answer1'),))
  
  bc_rule.bc_rule('domanda_gen_1_brutto_Coppia', This_rule_base, 'domanda1',
                  domanda_gen_1_brutto_Coppia, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('brutto_tempo'),
                   pattern.pattern_literal('Coppia'),
                   contexts.variable('answer1'),),
                  (),
                  (contexts.variable('answer1'),))
  
  bc_rule.bc_rule('domanda_gen_2_bello_Coppia', This_rule_base, 'domanda2',
                  domanda_gen_2_bello_Coppia, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('bel_tempo'),
                   pattern.pattern_literal('Coppia'),
                   pattern.pattern_literal('piace_natura'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))
  
  bc_rule.bc_rule('domanda_gen_2_brutto_Coppia', This_rule_base, 'domanda2',
                  domanda_gen_2_brutto_Coppia, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('brutto_tempo'),
                   pattern.pattern_literal('Coppia'),
                   pattern.pattern_literal('piace_storia'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))
  
  bc_rule.bc_rule('domada_gen_2_not_bello_Coppia', This_rule_base, 'domanda2',
                  domada_gen_2_not_bello_Coppia, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('bel_tempo'),
                   pattern.pattern_literal('Coppia'),
                   pattern.pattern_literal('no_piace_natura'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))
  
  bc_rule.bc_rule('domada_gen_2_not_brutto_Coppia', This_rule_base, 'domanda2',
                  domada_gen_2_not_brutto_Coppia, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('brutto_tempo'),
                   pattern.pattern_literal('Coppia'),
                   pattern.pattern_literal('no_piace_storia'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))
  
  bc_rule.bc_rule('domanda_gen_1_bello_Solo', This_rule_base, 'domanda1',
                  domanda_gen_1_bello_Solo, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('bel_tempo'),
                   pattern.pattern_literal('Solo'),
                   contexts.variable('answer1'),),
                  (),
                  (contexts.variable('answer1'),))
  
  bc_rule.bc_rule('domanda_gen_1_brutto_Solo', This_rule_base, 'domanda1',
                  domanda_gen_1_brutto_Solo, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('brutto_tempo'),
                   pattern.pattern_literal('Solo'),
                   contexts.variable('answer1'),),
                  (),
                  (contexts.variable('answer1'),))
  
  bc_rule.bc_rule('domanda_gen_2_bello_Solo', This_rule_base, 'domanda2',
                  domanda_gen_2_bello_Solo, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('bel_tempo'),
                   pattern.pattern_literal('Solo'),
                   pattern.pattern_literal('piace_natura'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))
  
  bc_rule.bc_rule('domanda_gen_2_brutto_Solo', This_rule_base, 'domanda2',
                  domanda_gen_2_brutto_Solo, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('brutto_tempo'),
                   pattern.pattern_literal('Solo'),
                   pattern.pattern_literal('piace_storia'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))
  
  bc_rule.bc_rule('domada_gen_2_not_bello_Solo', This_rule_base, 'domanda2',
                  domada_gen_2_not_bello_Solo, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('bel_tempo'),
                   pattern.pattern_literal('Solo'),
                   pattern.pattern_literal('no_piace_natura'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))
  
  bc_rule.bc_rule('domada_gen_2_not_brutto_Solo', This_rule_base, 'domanda2',
                  domada_gen_2_not_brutto_Solo, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('brutto_tempo'),
                   pattern.pattern_literal('Solo'),
                   pattern.pattern_literal('no_piace_storia'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))
  
  bc_rule.bc_rule('domanda_gen_1_bello_Affari', This_rule_base, 'domanda1',
                  domanda_gen_1_bello_Affari, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('bel_tempo'),
                   pattern.pattern_literal('Affari'),
                   contexts.variable('answer1'),),
                  (),
                  (contexts.variable('answer1'),))
  
  bc_rule.bc_rule('domanda_gen_1_brutto_Affari', This_rule_base, 'domanda1',
                  domanda_gen_1_brutto_Affari, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('brutto_tempo'),
                   pattern.pattern_literal('Affari'),
                   contexts.variable('answer1'),),
                  (),
                  (contexts.variable('answer1'),))
  
  bc_rule.bc_rule('domada_gen_2_not_bello_Affari', This_rule_base, 'domanda2',
                  domada_gen_2_not_bello_Affari, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('bel_tempo'),
                   pattern.pattern_literal('Affari'),
                   pattern.pattern_literal('no_sempre_occupato'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))
  
  bc_rule.bc_rule('domada_gen_2_not_brutto_Affari', This_rule_base, 'domanda2',
                  domada_gen_2_not_brutto_Affari, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('brutto_tempo'),
                   pattern.pattern_literal('Affari'),
                   pattern.pattern_literal('no_sempre_occupato'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))
  
  bc_rule.bc_rule('domanda_gen_1_bello_Famiglia_a', This_rule_base, 'domanda1',
                  domanda_gen_1_bello_Famiglia_a, None,
                  (pattern.pattern_literal('Avventuriera'),
                   pattern.pattern_literal('bel_tempo'),
                   pattern.pattern_literal('Famiglia'),
                   contexts.variable('answer1'),),
                  (),
                  (contexts.variable('answer1'),))
  
  bc_rule.bc_rule('domanda_gen_1_brutto_Famiglia_a', This_rule_base, 'domanda1',
                  domanda_gen_1_brutto_Famiglia_a, None,
                  (pattern.pattern_literal('Avventuriera'),
                   pattern.pattern_literal('brutto_tempo'),
                   pattern.pattern_literal('Famiglia'),
                   contexts.variable('answer1'),),
                  (),
                  (contexts.variable('answer1'),))
  
  bc_rule.bc_rule('domanda_gen_2_bello_Famiglia_a', This_rule_base, 'domanda2',
                  domanda_gen_2_bello_Famiglia_a, None,
                  (pattern.pattern_literal('Avventuriera'),
                   pattern.pattern_literal('bel_tempo'),
                   pattern.pattern_literal('Famiglia'),
                   pattern.pattern_literal('piace_natura'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))
  
  bc_rule.bc_rule('domanda_gen_2_brutto_Famiglia_a', This_rule_base, 'domanda2',
                  domanda_gen_2_brutto_Famiglia_a, None,
                  (pattern.pattern_literal('Avventuriera'),
                   pattern.pattern_literal('brutto_tempo'),
                   pattern.pattern_literal('Famiglia'),
                   pattern.pattern_literal('piace_bagnarsi'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))
  
  bc_rule.bc_rule('domada_gen_2_not_bello_Famiglia_a', This_rule_base, 'domanda2',
                  domada_gen_2_not_bello_Famiglia_a, None,
                  (pattern.pattern_literal('Avventuriera'),
                   pattern.pattern_literal('bel_tempo'),
                   pattern.pattern_literal('Famiglia'),
                   pattern.pattern_literal('no_piace_natura'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))
  
  bc_rule.bc_rule('domada_gen_2_not_brutto_Famiglia_a', This_rule_base, 'domanda2',
                  domada_gen_2_not_brutto_Famiglia_a, None,
                  (pattern.pattern_literal('Avventuriera'),
                   pattern.pattern_literal('brutto_tempo'),
                   pattern.pattern_literal('Famiglia'),
                   pattern.pattern_literal('no_piace_bagnarsi'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))
  
  bc_rule.bc_rule('domanda_gen_1_bello_Coppia_a', This_rule_base, 'domanda1',
                  domanda_gen_1_bello_Coppia_a, None,
                  (pattern.pattern_literal('Avventuriera'),
                   pattern.pattern_literal('bel_tempo'),
                   pattern.pattern_literal('Coppia'),
                   contexts.variable('answer1'),),
                  (),
                  (contexts.variable('answer1'),))
  
  bc_rule.bc_rule('domanda_gen_1_brutto_Coppia_a', This_rule_base, 'domanda1',
                  domanda_gen_1_brutto_Coppia_a, None,
                  (pattern.pattern_literal('Avventuriera'),
                   pattern.pattern_literal('brutto_tempo'),
                   pattern.pattern_literal('Coppia'),
                   contexts.variable('answer1'),),
                  (),
                  (contexts.variable('answer1'),))
  
  bc_rule.bc_rule('domanda_gen_2_bello_Coppia_a', This_rule_base, 'domanda2',
                  domanda_gen_2_bello_Coppia_a, None,
                  (pattern.pattern_literal('Avventuriera'),
                   pattern.pattern_literal('bel_tempo'),
                   pattern.pattern_literal('Coppia'),
                   pattern.pattern_literal('piace_natura'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))
  
  bc_rule.bc_rule('domanda_gen_2_brutto_Coppia_a', This_rule_base, 'domanda2',
                  domanda_gen_2_brutto_Coppia_a, None,
                  (pattern.pattern_literal('Avventuriera'),
                   pattern.pattern_literal('brutto_tempo'),
                   pattern.pattern_literal('Coppia'),
                   pattern.pattern_literal('piace_bagnarsi'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))
  
  bc_rule.bc_rule('domada_gen_2_not_bello_Coppia_a', This_rule_base, 'domanda2',
                  domada_gen_2_not_bello_Coppia_a, None,
                  (pattern.pattern_literal('Avventuriera'),
                   pattern.pattern_literal('bel_tempo'),
                   pattern.pattern_literal('Coppia'),
                   pattern.pattern_literal('no_piace_natura'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))
  
  bc_rule.bc_rule('domada_gen_2_not_brutto_Coppia_a', This_rule_base, 'domanda2',
                  domada_gen_2_not_brutto_Coppia_a, None,
                  (pattern.pattern_literal('Avventuriera'),
                   pattern.pattern_literal('brutto_tempo'),
                   pattern.pattern_literal('Coppia'),
                   pattern.pattern_literal('no_piace_bagnarsi'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))
  
  bc_rule.bc_rule('brutto_tempo', This_rule_base, 'bruttotempo',
                  brutto_tempo, None,
                  (contexts.variable('answer1'),),
                  (),
                  (pattern.pattern_literal('si'),
                   contexts.variable('answer1'),))
  
  bc_rule.bc_rule('no_brutto_tempo', This_rule_base, 'bruttotempo',
                  no_brutto_tempo, None,
                  (contexts.variable('answer1'),),
                  (),
                  (pattern.pattern_literal('no'),
                   contexts.variable('answer1'),))
  
  bc_rule.bc_rule('tempo_libero', This_rule_base, 'tempo_occupato',
                  tempo_libero, None,
                  (contexts.variable('answer1'),),
                  (),
                  (pattern.pattern_literal('Occupato'),
                   contexts.variable('answer1'),))
  
  bc_rule.bc_rule('no_tempo_libero', This_rule_base, 'tempo_occupato',
                  no_tempo_libero, None,
                  (contexts.variable('answer1'),),
                  (),
                  (pattern.pattern_literal('Libero'),
                   contexts.variable('answer1'),))
  
  bc_rule.bc_rule('bere_qualcosa', This_rule_base, 'bere',
                  bere_qualcosa, None,
                  (contexts.variable('answer1'),),
                  (),
                  (pattern.pattern_literal('si'),
                   contexts.variable('answer1'),))
  
  bc_rule.bc_rule('no_bere_qualcosa', This_rule_base, 'bere',
                  no_bere_qualcosa, None,
                  (contexts.variable('answer1'),),
                  (),
                  (pattern.pattern_literal('no'),
                   contexts.variable('answer1'),))
  
  bc_rule.bc_rule('piace_storia', This_rule_base, 'storia',
                  piace_storia, None,
                  (contexts.variable('answer1'),),
                  (),
                  (pattern.pattern_literal('si'),
                   contexts.variable('answer1'),))
  
  bc_rule.bc_rule('no_piace_storia', This_rule_base, 'storia',
                  no_piace_storia, None,
                  (contexts.variable('answer1'),),
                  (),
                  (pattern.pattern_literal('no'),
                   contexts.variable('answer1'),))
  
  bc_rule.bc_rule('piace_shopping', This_rule_base, 'shopping',
                  piace_shopping, None,
                  (contexts.variable('answer1'),),
                  (),
                  (pattern.pattern_literal('si'),
                   contexts.variable('answer1'),))
  
  bc_rule.bc_rule('no_piace_shopping', This_rule_base, 'shopping',
                  no_piace_shopping, None,
                  (contexts.variable('answer1'),),
                  (),
                  (pattern.pattern_literal('no'),
                   contexts.variable('answer1'),))
  
  bc_rule.bc_rule('scelta_tipo_vacanza_relax', This_rule_base, 'tipologia_vacanza',
                  scelta_tipo_vacanza_relax, None,
                  (contexts.variable('tipo_vacanza'),),
                  (),
                  (pattern.pattern_literal('Rilassante'),
                   contexts.variable('tipo_vacanza'),))
  
  bc_rule.bc_rule('scelta_tipo_vacanza_jamesbond', This_rule_base, 'tipologia_vacanza',
                  scelta_tipo_vacanza_jamesbond, None,
                  (contexts.variable('tipo_vacanza'),),
                  (),
                  (pattern.pattern_literal('Avventuriera'),
                   contexts.variable('tipo_vacanza'),))
  
  bc_rule.bc_rule('piace_sport', This_rule_base, 'sport',
                  piace_sport, None,
                  (contexts.variable('answer1'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('answer1'),))
  
  bc_rule.bc_rule('no_piace_sport', This_rule_base, 'sport',
                  no_piace_sport, None,
                  (contexts.variable('answer1'),),
                  (),
                  (pattern.pattern_literal(False),
                   contexts.variable('answer1'),))
  
  bc_rule.bc_rule('scelta_tipo_vacanza_divertimento', This_rule_base, 'tipologia_vacanza',
                  scelta_tipo_vacanza_divertimento, regole2_plans.scelta_tipo_vacanza_divertimento,
                  (contexts.variable('tipo_vacanza'),),
                  ('tipo_vacanza',),
                  (pattern.pattern_literal('Sfrenata'),
                   contexts.variable('plan#1'),))
  
  bc_rule.bc_rule('fine', This_rule_base, 'conclusione',
                  fine, None,
                  (contexts.variable('nucleo_fam'),
                   contexts.variable('meteo'),
                   contexts.variable('tipo_vacanza'),
                   contexts.variable('answer1'),
                   contexts.variable('answer2'),
                   contexts.variable('tipo'),),
                  (),
                  (contexts.variable('nucleo_fam'),
                   contexts.variable('meteo'),
                   contexts.variable('tipo_vacanza'),
                   contexts.variable('answer1'),
                   contexts.variable('answer2'),
                   contexts.variable('tipo'),))
  
  bc_rule.bc_rule('cosa_fare', This_rule_base, 'cosa_fare',
                  cosa_fare, None,
                  (contexts.variable('prev'),
                   contexts.variable('temperatura'),
                   contexts.variable('tipo'),),
                  (),
                  (contexts.variable('prev'),
                   contexts.variable('temperatura'),
                   contexts.variable('meteo'),
                   contexts.variable('nucleo_fam'),
                   contexts.variable('tipo_vacanza'),
                   contexts.variable('answer1'),
                   contexts.variable('answer2'),
                   contexts.variable('tipo'),))
  
  bc_rule.bc_rule('mangiare', This_rule_base, 'mangiare',
                  mangiare, None,
                  (contexts.variable('mangiare1'),),
                  (),
                  (pattern.pattern_literal('mangiare'),
                   contexts.variable('mangiare1'),))
  
  bc_rule.bc_rule('bere', This_rule_base, 'mangiare',
                  bere, None,
                  (contexts.variable('bere'),),
                  (),
                  (pattern.pattern_literal('bere'),
                   contexts.variable('bere'),))
  
  bc_rule.bc_rule('giochi', This_rule_base, 'giochi',
                  giochi, None,
                  (contexts.variable('gioco'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('gioco'),))
  
  bc_rule.bc_rule('no_giochi', This_rule_base, 'giochi',
                  no_giochi, None,
                  (contexts.variable('gioco'),),
                  (),
                  (pattern.pattern_literal(False),
                   contexts.variable('gioco'),))
  
  bc_rule.bc_rule('citta', This_rule_base, 'citta',
                  citta, None,
                  (contexts.variable('citta'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('citta'),))
  
  bc_rule.bc_rule('no_citta', This_rule_base, 'citta',
                  no_citta, None,
                  (contexts.variable('citta'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('citta'),))
  
  bc_rule.bc_rule('tipico', This_rule_base, 'tipico',
                  tipico, None,
                  (contexts.variable('tipico'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('tipico'),))
  
  bc_rule.bc_rule('no_tipico', This_rule_base, 'tipico',
                  no_tipico, None,
                  (contexts.variable('tipico'),),
                  (),
                  (pattern.pattern_literal(False),
                   contexts.variable('tipico'),))
  
  bc_rule.bc_rule('domanda_gen_1_amici_rilassante_brutto_tempo', This_rule_base, 'domanda1',
                  domanda_gen_1_amici_rilassante_brutto_tempo, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('brutto_tempo'),
                   pattern.pattern_literal('Amici'),
                   contexts.variable('answer1'),),
                  (),
                  (contexts.variable('answer1'),))
  
  bc_rule.bc_rule('domanda_gen_1_amici_rilassante_bel_tempo', This_rule_base, 'domanda1',
                  domanda_gen_1_amici_rilassante_bel_tempo, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('bel_tempo'),
                   pattern.pattern_literal('Amici'),
                   contexts.variable('answer1'),),
                  (),
                  (contexts.variable('answer1'),))
  
  bc_rule.bc_rule('domanda_gen_2_amici_rilassante_brutto_tempo', This_rule_base, 'domanda2',
                  domanda_gen_2_amici_rilassante_brutto_tempo, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('brutto_tempo'),
                   pattern.pattern_literal('Amici'),
                   pattern.pattern_literal('piace_tipico'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))
  
  bc_rule.bc_rule('domanda_gen_2_amici_rilassante_brutto_tempo_not', This_rule_base, 'domanda2',
                  domanda_gen_2_amici_rilassante_brutto_tempo_not, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('brutto_tempo'),
                   pattern.pattern_literal('Amici'),
                   pattern.pattern_literal('no_piace_tipico'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))
  
  bc_rule.bc_rule('domanda_gen_2_amici_rilassante_bel_tempo', This_rule_base, 'domanda2',
                  domanda_gen_2_amici_rilassante_bel_tempo, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('bel_tempo'),
                   pattern.pattern_literal('Amici'),
                   pattern.pattern_literal('piace_natura'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))
  
  bc_rule.bc_rule('domanda_gen_2_amici_rilassante_bel_tempo_not', This_rule_base, 'domanda2',
                  domanda_gen_2_amici_rilassante_bel_tempo_not, None,
                  (pattern.pattern_literal('Rilassante'),
                   pattern.pattern_literal('bel_tempo'),
                   pattern.pattern_literal('Amici'),
                   pattern.pattern_literal('no_piace_natura'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))
  
  bc_rule.bc_rule('domanda_gen_2_bello_Affari', This_rule_base, 'domanda2',
                  domanda_gen_2_bello_Affari, None,
                  (pattern.pattern_literal('Rilassante'),
                   contexts.variable('tempo'),
                   pattern.pattern_literal('Affari'),
                   pattern.pattern_literal('sempre_occupato'),
                   contexts.variable('answer2'),),
                  (),
                  (contexts.variable('answer2'),))


Krb_filename = '../regole2.krb'
Krb_lineno_map = (
    ((15, 19), (2, 2)),
    ((21, 28), (4, 4)),
    ((41, 45), (9, 9)),
    ((47, 52), (11, 11)),
    ((55, 55), (12, 12)),
    ((71, 75), (15, 15)),
    ((77, 82), (17, 17)),
    ((85, 85), (18, 18)),
    ((101, 105), (21, 21)),
    ((107, 112), (23, 23)),
    ((115, 115), (24, 24)),
    ((131, 135), (27, 27)),
    ((137, 142), (29, 29)),
    ((145, 145), (30, 30)),
    ((161, 165), (33, 33)),
    ((167, 172), (35, 35)),
    ((175, 175), (36, 36)),
    ((191, 195), (39, 39)),
    ((197, 202), (41, 41)),
    ((205, 205), (42, 42)),
    ((221, 225), (45, 45)),
    ((227, 232), (47, 47)),
    ((235, 235), (48, 48)),
    ((251, 255), (51, 51)),
    ((257, 262), (53, 53)),
    ((265, 265), (54, 54)),
    ((281, 285), (58, 58)),
    ((287, 292), (60, 60)),
    ((295, 295), (61, 61)),
    ((311, 315), (64, 64)),
    ((317, 322), (66, 66)),
    ((325, 325), (67, 67)),
    ((341, 345), (71, 71)),
    ((347, 352), (73, 73)),
    ((355, 355), (74, 74)),
    ((371, 375), (77, 77)),
    ((377, 382), (79, 79)),
    ((395, 399), (82, 82)),
    ((401, 406), (84, 84)),
    ((419, 423), (87, 87)),
    ((425, 430), (89, 89)),
    ((443, 447), (92, 92)),
    ((449, 454), (94, 94)),
    ((467, 471), (97, 97)),
    ((473, 478), (99, 99)),
    ((491, 495), (102, 102)),
    ((497, 502), (104, 104)),
    ((515, 519), (108, 108)),
    ((521, 526), (110, 110)),
    ((539, 543), (113, 113)),
    ((545, 550), (115, 115)),
    ((563, 567), (118, 118)),
    ((569, 574), (120, 120)),
    ((587, 591), (129, 129)),
    ((593, 598), (131, 131)),
    ((611, 615), (134, 134)),
    ((617, 622), (136, 136)),
    ((635, 639), (139, 139)),
    ((641, 646), (141, 141)),
    ((659, 663), (147, 147)),
    ((665, 670), (149, 149)),
    ((683, 687), (152, 152)),
    ((689, 694), (154, 154)),
    ((707, 711), (157, 157)),
    ((713, 718), (159, 159)),
    ((731, 735), (162, 162)),
    ((737, 742), (164, 164)),
    ((755, 759), (167, 167)),
    ((761, 766), (169, 169)),
    ((779, 783), (172, 172)),
    ((785, 790), (174, 174)),
    ((803, 807), (180, 180)),
    ((809, 814), (182, 182)),
    ((827, 831), (185, 185)),
    ((833, 838), (187, 187)),
    ((851, 855), (192, 192)),
    ((857, 862), (194, 194)),
    ((875, 879), (197, 197)),
    ((881, 886), (199, 199)),
    ((899, 903), (203, 203)),
    ((905, 910), (205, 205)),
    ((923, 927), (208, 208)),
    ((929, 934), (210, 210)),
    ((947, 951), (213, 213)),
    ((953, 958), (215, 215)),
    ((971, 975), (218, 218)),
    ((977, 982), (220, 220)),
    ((995, 999), (223, 223)),
    ((1001, 1006), (225, 225)),
    ((1019, 1023), (228, 228)),
    ((1025, 1030), (230, 230)),
    ((1043, 1047), (234, 234)),
    ((1049, 1054), (236, 236)),
    ((1067, 1071), (239, 239)),
    ((1073, 1078), (241, 241)),
    ((1091, 1095), (244, 244)),
    ((1097, 1102), (246, 246)),
    ((1115, 1119), (249, 249)),
    ((1121, 1126), (251, 251)),
    ((1139, 1143), (254, 254)),
    ((1145, 1150), (256, 256)),
    ((1163, 1167), (259, 259)),
    ((1169, 1174), (261, 261)),
    ((1187, 1191), (265, 265)),
    ((1193, 1198), (267, 267)),
    ((1201, 1201), (268, 268)),
    ((1217, 1221), (271, 271)),
    ((1223, 1228), (273, 273)),
    ((1231, 1231), (274, 274)),
    ((1247, 1251), (279, 279)),
    ((1253, 1258), (281, 281)),
    ((1261, 1261), (282, 282)),
    ((1277, 1281), (285, 285)),
    ((1283, 1288), (287, 287)),
    ((1291, 1291), (288, 288)),
    ((1307, 1311), (291, 291)),
    ((1313, 1318), (293, 293)),
    ((1321, 1321), (294, 294)),
    ((1337, 1341), (297, 297)),
    ((1343, 1348), (299, 299)),
    ((1351, 1351), (300, 300)),
    ((1367, 1371), (303, 303)),
    ((1373, 1378), (305, 305)),
    ((1381, 1381), (306, 306)),
    ((1397, 1401), (309, 309)),
    ((1403, 1408), (311, 311)),
    ((1411, 1411), (312, 312)),
    ((1427, 1431), (315, 315)),
    ((1433, 1438), (317, 317)),
    ((1441, 1441), (318, 318)),
    ((1457, 1461), (322, 322)),
    ((1463, 1468), (324, 324)),
    ((1471, 1471), (325, 325)),
    ((1487, 1491), (328, 328)),
    ((1493, 1498), (330, 330)),
    ((1501, 1501), (331, 331)),
    ((1517, 1521), (335, 335)),
    ((1523, 1528), (337, 337)),
    ((1531, 1531), (338, 338)),
    ((1547, 1551), (342, 342)),
    ((1553, 1558), (344, 344)),
    ((1561, 1561), (345, 345)),
    ((1577, 1581), (348, 348)),
    ((1583, 1588), (350, 350)),
    ((1591, 1591), (351, 351)),
    ((1607, 1611), (354, 354)),
    ((1613, 1622), (356, 356)),
    ((1636, 1640), (366, 366)),
    ((1642, 1652), (368, 368)),
    ((1665, 1669), (372, 372)),
    ((1671, 1678), (374, 374)),
    ((1679, 1684), (375, 375)),
    ((1685, 1690), (376, 376)),
    ((1691, 1699), (377, 377)),
    ((1700, 1709), (378, 378)),
    ((1710, 1720), (379, 379)),
    ((1733, 1737), (387, 387)),
    ((1739, 1744), (389, 389)),
    ((1747, 1747), (390, 390)),
    ((1763, 1767), (394, 394)),
    ((1769, 1774), (396, 396)),
    ((1777, 1777), (397, 397)),
    ((1793, 1797), (400, 400)),
    ((1799, 1804), (402, 402)),
    ((1807, 1807), (403, 403)),
    ((1823, 1827), (406, 406)),
    ((1829, 1834), (408, 408)),
    ((1837, 1837), (409, 409)),
    ((1853, 1857), (413, 413)),
    ((1859, 1864), (415, 415)),
    ((1867, 1867), (416, 416)),
    ((1883, 1887), (419, 419)),
    ((1889, 1894), (421, 421)),
    ((1897, 1897), (422, 422)),
    ((1913, 1917), (426, 426)),
    ((1919, 1924), (428, 428)),
    ((1927, 1927), (429, 429)),
    ((1943, 1947), (432, 432)),
    ((1949, 1954), (434, 434)),
    ((1957, 1957), (435, 435)),
    ((1973, 1977), (441, 441)),
    ((1979, 1984), (443, 443)),
    ((1997, 2001), (447, 447)),
    ((2003, 2008), (449, 449)),
    ((2021, 2025), (452, 452)),
    ((2027, 2032), (454, 454)),
    ((2045, 2049), (458, 458)),
    ((2051, 2056), (460, 460)),
    ((2069, 2073), (463, 463)),
    ((2075, 2080), (465, 465)),
    ((2093, 2097), (469, 469)),
    ((2099, 2104), (471, 471)),
    ((2117, 2121), (476, 476)),
    ((2123, 2128), (478, 478)),
)
