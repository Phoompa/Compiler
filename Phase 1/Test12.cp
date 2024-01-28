using Godot;
using System;

public partial class main_menu : Control
{
	// Reference to the Options node


	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{

		// Get a reference to the Options node
		var options = GetNode<Control>("Options");
		options.Visible = false;
		// Connect the button's pressed signal to the _on_Button2_pressed method
		Button button2 = GetNode<Button>("MainMenuContainer/Button2");
		button2.Connect("pressed", new Callable(this,nameof(_on_Button2_pressed)));
		
		//Handle when audio button is clicked inside Options node
		Button audioButton = GetNode<Button>("/root/MainMenu/Options/VBoxContainer/Button4");
		audioButton.Connect("pressed", new Callable(this,nameof(_on_audio_pressed)));
		
		//Handle when back button in Options is clicked
		Button backButtonOptions = GetNode<Button>("/root/MainMenu/Options/OptionsBack");
		backButtonOptions.Connect("pressed", new Callable(this,nameof(_on_backButtonOptions_pressed)));
		// Handle when back button is clicked in Audio
		Button backButtonAudio = GetNode<Button>("/root/MainMenu/Options/Audio/AudioBack");
		backButtonAudio.Connect("pressed",new Callable(this,nameof(_on_backButtonAudio_pressed)));
		
		//Music slider
		HSlider musicSlider = GetNode<HSlider>("/root/MainMenu/Options/Audio/HBoxContainer/Slider/Music");
		musicSlider.Connect("value_changed",new Callable(this,nameof(_on_music_slider_changed)));
		
		//Sound effect slider
		HSlider SFXSlider = GetNode<HSlider>("/root/MainMenu/Options/Audio/HBoxContainer/Slider/SFX");
		SFXSlider.Connect("value_changed",new Callable(this,nameof(_on_SFX_slider_changed)));
		
		//Master Slider
		HSlider masterSlider = GetNode<HSlider>("/root/MainMenu/Options/Audio/HBoxContainer/Slider/Master");
		masterSlider.Connect("value_changed",new Callable(this,nameof(_on_master_slider_changed)));
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
		// Your _Process code here
	}
	//Called when master slider is changed
	private void _on_master_slider_changed(float value){
		var bus_index = AudioServer.GetBusIndex("Master");
		AudioServer.SetBusVolumeDb(bus_index,value);
		if(value == -10){
			AudioServer.SetBusMute(bus_index,true);
		} else{
			AudioServer.SetBusMute(bus_index,false);
			AudioServer.SetBusVolumeDb(bus_index,value);
		}
		
	}
	//called when sfx slider is changed
	private void _on_SFX_slider_changed(float value){
		var bus_index = AudioServer.GetBusIndex("SFX");
		GD.Print(value);
		AudioServer.SetBusVolumeDb(bus_index,value);
		if(value == -40){
			AudioServer.SetBusMute(bus_index,true);
		} else{
			AudioServer.SetBusMute(bus_index,false);
			AudioServer.SetBusVolumeDb(bus_index,value);
		}
		
	}
	//called when music slider is changed
	private void _on_music_slider_changed(float value){
		var bus_index = AudioServer.GetBusIndex("Music");
		AudioServer.SetBusVolumeDb(bus_index,value);
		if(value == -40){
			AudioServer.SetBusMute(bus_index,true);
		} else{
			AudioServer.SetBusMute(bus_index,false);
			AudioServer.SetBusVolumeDb(bus_index,value);
		}
		
	}
	// Called when Button2 is pressed
	private void _on_Button2_pressed()
	{
		var options = GetNode<Control>("/root/MainMenu/Options");
		var MainMenuContainer = GetNode<VBoxContainer>("/root/MainMenu/MainMenuContainer");
		var audio = GetNode<Control>("/root/MainMenu/Options/Audio");
		// Make Options visible
		// Make MainMenu invisible
		MainMenuContainer.Visible = false;
		audio.Visible = false;
		options.Visible = true;
	}
	// called when audio button is pressed in Options 
	private void _on_audio_pressed(){

		var optionsVBox = GetNode<VBoxContainer>("/root/MainMenu/Options/VBoxContainer");
		var audio = GetNode<Control>("/root/MainMenu/Options/Audio");
		Button backButtonOptions = GetNode<Button>("/root/MainMenu/Options/OptionsBack");
		Button backButtonAudio = GetNode<Button>("/root/MainMenu/Options/Audio/AudioBack");
		//Make componenets in optionVBox invisible and audio components visible
		optionsVBox.Visible = false;
		audio.Visible = true;
		backButtonOptions.Visible = false;
		backButtonAudio.Visible = true;
		
		//plays sound effect to test
		var audioPlayer = GetNode<AudioStreamPlayer>("/root/MainMenu/SoundEffect");
		audioPlayer.Play();
	}
	
	private void _on_backButtonOptions_pressed(){
		var options = GetNode<Control>("/root/MainMenu/Options");
		var MainMenuContainer = GetNode<VBoxContainer>("/root/MainMenu/MainMenuContainer");
		// make optionsVBox invisible and make MainMenuContainer visible
		options.Visible = false;
		MainMenuContainer.Visible= true;

	}
	
	private void _on_backButtonAudio_pressed(){
		var optionsVBox = GetNode<VBoxContainer>("/root/MainMenu/Options/VBoxContainer");
		var audio = GetNode<Control>("/root/MainMenu/Options/Audio");
		Button backButtonOptions = GetNode<Button>("/root/MainMenu/Options/OptionsBack");
		Button backButtonAudio = GetNode<Button>("/root/MainMenu/Options/Audio/AudioBack");
		//make audio components invisible and make optionsVBox components Visible
		audio.Visible = false;
		backButtonAudio.Visible = false;
		optionsVBox.Visible = true;
		backButtonOptions.Visible = true;
	}
}def
Fed
If
Then
Else
Fi
While
Do
Od
Print
Return
Or
And
Not
=
+
-
*
/
%
<
>
==
<=
>=
<>
,
;
(
)
a
asdsasd
a21
1
19
123.345