RandomFunction = {
  floor random[0,1,2];
};

GenerateRandomData = {
  private ["_y","_counter", "_array","_return","_counts","_percents","_z","_w","_count"];
  _counter = 0;
  _array = [];
  _counts = [];
  _percents = [];
  _z = 1000;
  while {_counter < _z } do
  {
      _y = call RandomFunction;
      _array pushBack _y;
      _counter = _counter + 1;
  };
  {

      _found = [_x, _counts] call objFinder;
    if(isNil "_found") then {
      _w = _x;
      _count = {_x == _w} count _array;
      _counts pushback [_x,_count] ;
      _percents pushBack [_x,(_count/ (_z / 100))];
    };
  } forEach _array;

   _return = [_array,_counts,_percents];
   _return;
};

Visualise = {
  private ["_y","_str","_subs","_cnt"];
  _y = call GenerateRandomData;
  _str = [];
  {
    _subs = format ["%1%2 : ",_x select 1,"%"];
    _cnt = 0;
    while {_cnt < (round (_x select 1))} do {
      _cnt = _cnt + 5;
      _subs = _subs + "*";
    };
    _str pushBack _subs;
  } forEach (_y select 2);
  systemChat format ["%1",_str];
  "RNG Visualiser" hintC _str;
};

objFinder = {
  private ["_return"];
  _return = nil;
  {
      if(_x select 0 == _this select 0) then {
        _return  = _x select 1;
      };
  } forEach (_this select 1);
  _return;
}
