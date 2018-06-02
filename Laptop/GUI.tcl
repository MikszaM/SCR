#############################################################################
# Generated by PAGE version 4.13
# in conjunction with Tcl version 8.6
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #d8d8d8
set vTcl(active_menu_fg) #000000
}

#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top37
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top37
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top37 {base} {
    if {$base == ""} {
        set base .top37
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background {#d9d9d9} -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 460x300+587+320
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1905 930
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "SCR"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    radiobutton $top.rad38 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -command sel -foreground {#000000} \
        -highlightcolor black -justify left -takefocus 0 -text Bluetooth \
        -value 1 -variable Radio 
    vTcl:DefineAlias "$top.rad38" "Radiobutton1" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad39 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -command sel -foreground {#000000} \
        -highlightcolor black -justify left -overrelief ridge -takefocus 0 \
        -text TCP -value 2 -variable Radio 
    vTcl:DefineAlias "$top.rad39" "Radiobutton2" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad40 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -command sel -foreground {#000000} \
        -highlightcolor black -justify left -takefocus 0 -text UDP -value 3 \
        -variable Radio 
    vTcl:DefineAlias "$top.rad40" "Radiobutton3" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad41 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -command sel -foreground {#000000} \
        -highlightcolor black -justify left -takefocus 0 -text HTTP -value 4 \
        -variable Radio 
    vTcl:DefineAlias "$top.rad41" "Radiobutton4" vTcl:WidgetProc "Toplevel1" 1
    button $top.but42 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -command Send -foreground {#000000} \
        -highlightcolor black -takefocus 0 -text Send 
    vTcl:DefineAlias "$top.but42" "Button1" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent44 \
        -background white -font TkFixedFont -foreground {#000000} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black -takefocus 0 \
        -textvariable DataSend 
    vTcl:DefineAlias "$top.ent44" "Entry1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab45 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -text {[Light number] [on/off]} 
    vTcl:DefineAlias "$top.lab45" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab47 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -text Commands: 
    vTcl:DefineAlias "$top.lab47" "Label3" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab48 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -text Info -textvariable Info 
    vTcl:DefineAlias "$top.lab48" "Label4" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab38 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -text {Data received} 
    vTcl:DefineAlias "$top.lab38" "Label5" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab39 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -text {Data to send} 
    vTcl:DefineAlias "$top.lab39" "Label6" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab42 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -relief ridge -textvariable DataRec 
    vTcl:DefineAlias "$top.lab42" "Label7" vTcl:WidgetProc "Toplevel1" 1
    button $top.but38 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -command Run_Servers -foreground {#000000} \
        -highlightcolor black -text {Run servers} 
    vTcl:DefineAlias "$top.but38" "Button2" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab40 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -text {[1,2,0-both] [on,off]} 
    vTcl:DefineAlias "$top.lab40" "Label1_1" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.rad38 \
        -in $top -x 300 -y 40 -anchor nw -bordermode ignore 
    place $top.rad39 \
        -in $top -x 300 -y 90 -anchor nw -bordermode ignore 
    place $top.rad40 \
        -in $top -x 300 -y 140 -width 54 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.rad41 \
        -in $top -x 300 -y 190 -anchor nw -bordermode ignore 
    place $top.but42 \
        -in $top -x 370 -y 70 -width 77 -relwidth 0 -height 37 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent44 \
        -in $top -x 120 -y 40 -anchor nw -bordermode ignore 
    place $top.lab45 \
        -in $top -x 110 -y 80 -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 20 -y 80 -anchor nw -bordermode ignore 
    place $top.lab48 \
        -in $top -x 30 -y 220 -anchor nw -bordermode ignore 
    place $top.lab38 \
        -in $top -x 20 -y 170 -anchor nw -bordermode ignore 
    place $top.lab39 \
        -in $top -x 20 -y 40 -anchor nw -bordermode ignore 
    place $top.lab42 \
        -in $top -x 120 -y 170 -width 106 -relwidth 0 -height 29 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but38 \
        -in $top -x 370 -y 130 -width 77 -relwidth 0 -height 37 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab40 \
        -in $top -x 110 -y 120 -width 156 -height 19 -anchor nw \
        -bordermode inside 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top37 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

