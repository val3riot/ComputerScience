cell(0,0).
cell(1,1).
cell(1,2).
cell(1,3).
cell(1,4).
cell(1,5).
cell(2,1).
cell(2,2).
cell(2,5).
cell(3,1).
cell(3,2).
cell(3,5).
cell(4,1).
cell(4,2).
cell(4,3).
cell(4,4).
cell(4,5).
cell(5,1).
cell(5,2).
cell(5,3).
cell(5,4).
cell(5,5).
% Prima riga
link(cell(0,0), cell(1,0)).
link(cell(0,0), cell(0,1)).
link(cell(0,1), cell(0,0)).
link(cell(0,1), cell(1,1)).
link(cell(0,2), cell(0,1)).
link(cell(0,2), cell(1,2)).
link(cell(0,3), cell(0,2)).
link(cell(0,3), cell(1,3)).
link(cell(0,4), cell(0,3)).
link(cell(0,4), cell(1,4)).
link(cell(0,5), cell(0,4)).
link(cell(0,5), cell(1,5)).

% Seconda riga
link(cell(1,0), cell(0,0)).
link(cell(1,0), cell(2,0)).
link(cell(1,1), cell(0,1)).
link(cell(1,1), cell(1,0)).
link(cell(1,1), cell(1,2)).
link(cell(1,2), cell(0,2)).
link(cell(1,2), cell(2,2)).
link(cell(1,3), cell(0,3)).
link(cell(1,3), cell(1,2)).
link(cell(1,3), cell(2,3)).
link(cell(1,4), cell(0,4)).
link(cell(1,4), cell(1,3)).
link(cell(1,4), cell(2,4)).
link(cell(1,5), cell(0,5)).
link(cell(1,5), cell(1,4)).
link(cell(1,5), cell(2,5)).

% Terza riga
link(cell(2,0), cell(1,0)).
link(cell(2,0), cell(3,0)).
link(cell(2,1), cell(1,1)).
link(cell(2,1), cell(2,0)).
link(cell(2,1), cell(2,2)).
link(cell(2,2), cell(1,2)).
link(cell(2,2), cell(3,2)).
link(cell(2,3), cell(1,3)).
link(cell(2,3), cell(2,2)).
link(cell(2,3), cell(3,3)).
link(cell(2,4), cell(1,4)).
link(cell(2,4), cell(2,3)).
link(cell(2,4), cell(3,4)).
link(cell(2,5), cell(1,5)).
link(cell(2,5), cell(2,4)).
link(cell(2,5), cell(3,5)).

% Quarta riga
link(cell(3,0), cell(2,0)).
link(cell(3,0), cell(4,0)).
link(cell(3,1), cell(2,1)).
link(cell(3,1), cell(3,0)).
link(cell(3,1), cell(3,2)).
link(cell(3,2), cell(2,2)).
link(cell(3,2), cell(4,2)).
link(cell(3,3), cell(2,3)).
link(cell(3,3), cell(3,2)).
link(cell(3,3), cell(4,3)).
link(cell(3,4), cell(2,4)).
link(cell(3,4), cell(3,3)).
link(cell(3,4), cell(4,4)).
link(cell(3,5), cell(2,5)).
link(cell(3,5), cell(3,4)).
link(cell(3,5), cell(4,5)).

% Quinta riga
link(cell(4,0), cell(3,0)).
link(cell(4,0), cell(5,0)).
link(cell(4,1), cell(3,1)).
link(cell(4,1), cell(4,0)).
link(cell(4,1), cell(4,2)).
link(cell(4,2), cell(3,2)).
link(cell(4,2), cell(5,2)).
link(cell(4,3), cell(3,3)).
link(cell(4,3), cell(4,2)).
link(cell(4,3), cell(5,3)).
link(cell(4,4), cell(3,4)).
link(cell(4,4), cell(4,3)).
link(cell(4,4), cell(5,4)).
link(cell(4,5), cell(3,5)).
link(cell(4,5), cell(4,4)).
link(cell(4,5), cell(5,5)).

% Sesta riga (ultima)
link(cell(5,0), cell(4,0)).
link(cell(5,1), cell(4,1)).
link(cell(5,1), cell(5,0)).
link(cell(5,1), cell(5,2)).
link(cell(5,2), cell(4,2)).
link(cell(5,2), cell(5,1)).
link(cell(5,2), cell(5,3)).
link(cell(5,3), cell(4,3)).
link(cell(5,3), cell(5,2)).
link(cell(5,3), cell(5,4)).
link(cell(5,4), cell(4,4)).
link(cell(5,4), cell(5,3)).
link(cell(5,4), cell(5,5)).
link(cell(5,5), cell(4,5)).
link(cell(5,5), cell(5,4)).
% Predicato per trovare il cammino minimo tra due celle
bfs(Path, Start, End) :-
    bfs([[Start]], End, Path).
bfs([[End|Tail]|_], End, [End|Tail]).
bfs([Path|Paths], End, Result) :-
    Path = [Current|_],
    findall([Next,Current|Path],
            (link(Current, Next), \+ member(Next, Path)),
            NewPaths),
    append(Paths, NewPaths, Paths1),
    bfs(Paths1, End, Result).
