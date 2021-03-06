
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BIGGER BOUNCEBALL CANVAS CIRCLE LEFT LINE MIRRORX MIRRORY MOVE NUMBER OVAL QUOT RECT RIGHT ROTATE SHOW SMALLER TEXT WRDexpression : NUMBERcolor : QUOT WRD QUOTx-coor : NUMBERy-coor : NUMBERradius : NUMBERdegrees : NUMBERspeed : WRDdirection : WRDexpression : CANVAS expression expression color\n                  | CANVAS expression expressionexpression : LINE x-coor y-coor x-coor y-coor color\n                  | LINE x-coor y-coor x-coor y-coorexpression : CIRCLE x-coor y-coor radius color\n                  | CIRCLE x-coor y-coor radiusexpression : OVAL x-coor y-coor x-coor y-coor color\n                  | OVAL x-coor y-coor x-coor y-coorexpression : RECT x-coor y-coor x-coor y-coor color\n                  | RECT x-coor y-coor x-coor y-coorexpression : TEXT x-coor y-coor QUOT WRD QUOTexpression : MOVE speed directionexpression : ROTATE LEFT degrees\n                  | ROTATE RIGHT degreesexpression : BIGGER\n                  | SMALLER\n                  | BIGGER SHOW\n                  | SMALLER SHOWexpression : MIRRORX\n                  | MIRRORYexpression : BOUNCEBALL'
    
_lr_action_items = {'NUMBER':([0,2,3,4,5,6,7,8,11,12,13,14,15,16,17,18,19,20,21,22,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,43,44,45,46,47,50,51,52,53,55,56,57,58,59,],[2,-1,2,18,18,18,18,18,-23,-24,-27,-28,-29,2,31,-3,31,31,31,31,39,39,-25,-26,-10,18,-4,45,18,18,-20,-8,-21,-6,-22,-9,31,-14,-5,31,31,-12,-13,-16,-18,-2,-11,-15,-17,-19,]),'CANVAS':([0,2,3,11,12,13,14,15,16,27,28,29,31,36,37,38,39,40,41,44,45,50,51,52,53,55,56,57,58,59,],[3,-1,3,-23,-24,-27,-28,-29,3,-25,-26,-10,-4,-20,-8,-21,-6,-22,-9,-14,-5,-12,-13,-16,-18,-2,-11,-15,-17,-19,]),'LINE':([0,2,3,11,12,13,14,15,16,27,28,29,31,36,37,38,39,40,41,44,45,50,51,52,53,55,56,57,58,59,],[4,-1,4,-23,-24,-27,-28,-29,4,-25,-26,-10,-4,-20,-8,-21,-6,-22,-9,-14,-5,-12,-13,-16,-18,-2,-11,-15,-17,-19,]),'CIRCLE':([0,2,3,11,12,13,14,15,16,27,28,29,31,36,37,38,39,40,41,44,45,50,51,52,53,55,56,57,58,59,],[5,-1,5,-23,-24,-27,-28,-29,5,-25,-26,-10,-4,-20,-8,-21,-6,-22,-9,-14,-5,-12,-13,-16,-18,-2,-11,-15,-17,-19,]),'OVAL':([0,2,3,11,12,13,14,15,16,27,28,29,31,36,37,38,39,40,41,44,45,50,51,52,53,55,56,57,58,59,],[6,-1,6,-23,-24,-27,-28,-29,6,-25,-26,-10,-4,-20,-8,-21,-6,-22,-9,-14,-5,-12,-13,-16,-18,-2,-11,-15,-17,-19,]),'RECT':([0,2,3,11,12,13,14,15,16,27,28,29,31,36,37,38,39,40,41,44,45,50,51,52,53,55,56,57,58,59,],[7,-1,7,-23,-24,-27,-28,-29,7,-25,-26,-10,-4,-20,-8,-21,-6,-22,-9,-14,-5,-12,-13,-16,-18,-2,-11,-15,-17,-19,]),'TEXT':([0,2,3,11,12,13,14,15,16,27,28,29,31,36,37,38,39,40,41,44,45,50,51,52,53,55,56,57,58,59,],[8,-1,8,-23,-24,-27,-28,-29,8,-25,-26,-10,-4,-20,-8,-21,-6,-22,-9,-14,-5,-12,-13,-16,-18,-2,-11,-15,-17,-19,]),'MOVE':([0,2,3,11,12,13,14,15,16,27,28,29,31,36,37,38,39,40,41,44,45,50,51,52,53,55,56,57,58,59,],[9,-1,9,-23,-24,-27,-28,-29,9,-25,-26,-10,-4,-20,-8,-21,-6,-22,-9,-14,-5,-12,-13,-16,-18,-2,-11,-15,-17,-19,]),'ROTATE':([0,2,3,11,12,13,14,15,16,27,28,29,31,36,37,38,39,40,41,44,45,50,51,52,53,55,56,57,58,59,],[10,-1,10,-23,-24,-27,-28,-29,10,-25,-26,-10,-4,-20,-8,-21,-6,-22,-9,-14,-5,-12,-13,-16,-18,-2,-11,-15,-17,-19,]),'BIGGER':([0,2,3,11,12,13,14,15,16,27,28,29,31,36,37,38,39,40,41,44,45,50,51,52,53,55,56,57,58,59,],[11,-1,11,-23,-24,-27,-28,-29,11,-25,-26,-10,-4,-20,-8,-21,-6,-22,-9,-14,-5,-12,-13,-16,-18,-2,-11,-15,-17,-19,]),'SMALLER':([0,2,3,11,12,13,14,15,16,27,28,29,31,36,37,38,39,40,41,44,45,50,51,52,53,55,56,57,58,59,],[12,-1,12,-23,-24,-27,-28,-29,12,-25,-26,-10,-4,-20,-8,-21,-6,-22,-9,-14,-5,-12,-13,-16,-18,-2,-11,-15,-17,-19,]),'MIRRORX':([0,2,3,11,12,13,14,15,16,27,28,29,31,36,37,38,39,40,41,44,45,50,51,52,53,55,56,57,58,59,],[13,-1,13,-23,-24,-27,-28,-29,13,-25,-26,-10,-4,-20,-8,-21,-6,-22,-9,-14,-5,-12,-13,-16,-18,-2,-11,-15,-17,-19,]),'MIRRORY':([0,2,3,11,12,13,14,15,16,27,28,29,31,36,37,38,39,40,41,44,45,50,51,52,53,55,56,57,58,59,],[14,-1,14,-23,-24,-27,-28,-29,14,-25,-26,-10,-4,-20,-8,-21,-6,-22,-9,-14,-5,-12,-13,-16,-18,-2,-11,-15,-17,-19,]),'BOUNCEBALL':([0,2,3,11,12,13,14,15,16,27,28,29,31,36,37,38,39,40,41,44,45,50,51,52,53,55,56,57,58,59,],[15,-1,15,-23,-24,-27,-28,-29,15,-25,-26,-10,-4,-20,-8,-21,-6,-22,-9,-14,-5,-12,-13,-16,-18,-2,-11,-15,-17,-19,]),'$end':([1,2,11,12,13,14,15,27,28,29,31,36,37,38,39,40,41,44,45,50,51,52,53,55,56,57,58,59,],[0,-1,-23,-24,-27,-28,-29,-25,-26,-10,-4,-20,-8,-21,-6,-22,-9,-14,-5,-12,-13,-16,-18,-2,-11,-15,-17,-19,]),'QUOT':([2,11,12,13,14,15,27,28,29,31,35,36,37,38,39,40,41,44,45,49,50,51,52,53,54,55,56,57,58,59,],[-1,-23,-24,-27,-28,-29,-25,-26,42,-4,48,-20,-8,-21,-6,-22,-9,42,-5,55,42,-13,42,42,59,-2,-11,-15,-17,-19,]),'WRD':([9,23,24,42,48,],[24,37,-7,49,54,]),'LEFT':([10,],[25,]),'RIGHT':([10,],[26,]),'SHOW':([11,12,],[27,28,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,3,16,],[1,16,29,]),'x-coor':([4,5,6,7,8,30,33,34,],[17,19,20,21,22,43,46,47,]),'speed':([9,],[23,]),'y-coor':([17,19,20,21,22,43,46,47,],[30,32,33,34,35,50,52,53,]),'direction':([23,],[36,]),'degrees':([25,26,],[38,40,]),'color':([29,44,50,52,53,],[41,51,56,57,58,]),'radius':([32,],[44,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser_dl.py',27),
  ('color -> QUOT WRD QUOT','color',3,'p_expression_color','parser_dl.py',31),
  ('x-coor -> NUMBER','x-coor',1,'p_expression_xcoor','parser_dl.py',35),
  ('y-coor -> NUMBER','y-coor',1,'p_expression_ycoor','parser_dl.py',39),
  ('radius -> NUMBER','radius',1,'p_expression_radius','parser_dl.py',43),
  ('degrees -> NUMBER','degrees',1,'p_expression_degrees','parser_dl.py',47),
  ('speed -> WRD','speed',1,'p_expression_speed','parser_dl.py',51),
  ('direction -> WRD','direction',1,'p_expression_direction','parser_dl.py',55),
  ('expression -> CANVAS expression expression color','expression',4,'p_expression_canvas','parser_dl.py',59),
  ('expression -> CANVAS expression expression','expression',3,'p_expression_canvas','parser_dl.py',60),
  ('expression -> LINE x-coor y-coor x-coor y-coor color','expression',6,'p_expression_line','parser_dl.py',71),
  ('expression -> LINE x-coor y-coor x-coor y-coor','expression',5,'p_expression_line','parser_dl.py',72),
  ('expression -> CIRCLE x-coor y-coor radius color','expression',5,'p_expression_circle','parser_dl.py',87),
  ('expression -> CIRCLE x-coor y-coor radius','expression',4,'p_expression_circle','parser_dl.py',88),
  ('expression -> OVAL x-coor y-coor x-coor y-coor color','expression',6,'p_expression_oval','parser_dl.py',108),
  ('expression -> OVAL x-coor y-coor x-coor y-coor','expression',5,'p_expression_oval','parser_dl.py',109),
  ('expression -> RECT x-coor y-coor x-coor y-coor color','expression',6,'p_expression_rectangle','parser_dl.py',127),
  ('expression -> RECT x-coor y-coor x-coor y-coor','expression',5,'p_expression_rectangle','parser_dl.py',128),
  ('expression -> TEXT x-coor y-coor QUOT WRD QUOT','expression',6,'p_expression_text','parser_dl.py',140),
  ('expression -> MOVE speed direction','expression',3,'p_expression_move','parser_dl.py',145),
  ('expression -> ROTATE LEFT degrees','expression',3,'p_expression_rotate','parser_dl.py',175),
  ('expression -> ROTATE RIGHT degrees','expression',3,'p_expression_rotate','parser_dl.py',176),
  ('expression -> BIGGER','expression',1,'p_expression_scale','parser_dl.py',208),
  ('expression -> SMALLER','expression',1,'p_expression_scale','parser_dl.py',209),
  ('expression -> BIGGER SHOW','expression',2,'p_expression_scale','parser_dl.py',210),
  ('expression -> SMALLER SHOW','expression',2,'p_expression_scale','parser_dl.py',211),
  ('expression -> MIRRORX','expression',1,'p_expression_mirror','parser_dl.py',256),
  ('expression -> MIRRORY','expression',1,'p_expression_mirror','parser_dl.py',257),
  ('expression -> BOUNCEBALL','expression',1,'p_expression_bounceball','parser_dl.py',328),
]
