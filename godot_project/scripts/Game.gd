extends Node2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	$Player1.player_name = "Player 1"
	$Player1/name.text = $Player1.player_name
	
	$Player2.player_name = "Player 2"
	$Player2/name.text = $Player2.player_name
	
	$Player3.player_name = "Player 3"
	$Player3/name.text = $Player3.player_name
	
	$Player4.player_name = "Player 4"
	$Player4/name.text = $Player4.player_name
	
	$Player5.player_name = "Player 5"
	$Player5/name.text = $Player5.player_name


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
