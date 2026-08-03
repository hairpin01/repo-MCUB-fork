# name: OpenAgent
# version: 0.8.0-main.build:1043
# CubKit build info:
# CubKit source sha256: bc682f65e9fd2565a885e2ac1450c097cecb6c92a0dbcfe62a14a812fe5369ce
# CubKit payload sha256: 602acffb8794c82d1da0f25cecb6036da664d0cb35fb6d7a95d08fb0876fe995
# CubKit signature: 0e4f67ac24e16a8dc1481a313f0744b02ca9a4e19bf58cfd357ba3b70cbf20ee
# CubKit signature algorithm: sha256(cubkit-sign-v1 + module id + source sha256 + payload sha256)
# CubKit source map:
# - generated line 1608 -> OpenAgentMain.py:1
# - bundled files are extracted from the CubKit payload at import time:
#   - MCUBEvent.py -> MCUBEvent.py:1 (lines: 74, sha256: 684c8469682b5fda32ca4c6fa9d5b880926c95b2354165be7212a257f6625741)
#   - OpenAgentLib/ContextService.py -> ContextService.py:1 (lines: 604, sha256: 49c7bd66e2fff87d9c2c3b3db3f6697305e6b3804d36d68a586ca319fa1fb141)
#   - OpenAgentLib/Lifecycle.py -> Lifecycle.py:1 (lines: 146, sha256: 77efe289287f864c4cb021e7e94ddfe53ced35f634d0fc388db47da60749fbe7)
#   - OpenAgentLib/Manager/OASession.py -> OASession.py:1 (lines: 44, sha256: cfcd3aaf4107518327a30565e98d0b721e7b1a3a530edc20eedf2ffa4779106c)
#   - OpenAgentLib/Manager/Session.py -> Session.py:1 (lines: 837, sha256: b388be5fd870ad81a1c28dc022c1055657bad33ddb4aaedf7b8dcf0696bbb687)
#   - OpenAgentLib/Manager/__init__.py -> __init__.py:1 (lines: 8, sha256: 9313361e9fffe9d3b9191017eabb6b610e217d111680eb26468d5ce68d782975)
#   - OpenAgentLib/OpenAgentMixins.py -> OpenAgentMixins.py:1 (lines: 87, sha256: cdd407e49027900c5eef6dd63c53484749b8999c307b6181ddc7518623778ec2)
#   - OpenAgentLib/Placeholders.py -> Placeholders.py:1 (lines: 343, sha256: dccfb5d492c85e69671a93cc25c50286b0dd2be892d573af07c8f31c1588f4fd)
#   - OpenAgentLib/Plugin/PluginBase.py -> PluginBase.py:1 (lines: 365, sha256: c9b19c77606dfb58f1725a96698d4dd47dbdb1575cd41553634c4ffa752b9319)
#   - OpenAgentLib/Plugin/PluginsEngine.py -> PluginsEngine.py:1 (lines: 2951, sha256: d38f5af4a42461a0d1dfa65b5c83e423ff71f7dabc408e304c03fd834330741d)
#   - OpenAgentLib/ResponseAgent.py -> ResponseAgent.py:1 (lines: 774, sha256: d19a6157bdc10fc2c6106f2709778974dd35f1e3c42e5ae625b88859becc2e01)
#   - OpenAgentLib/SystemPlugins/Code/attach_result.py -> attach_result.py:1 (lines: 21, sha256: 4fd61f896f0adf5cc5c69ad288e3d54b61966bd2f2662703ade67586f69f29d9)
#   - OpenAgentLib/SystemPlugins/Code/choose_filename.py -> choose_filename.py:1 (lines: 21, sha256: 2a5087f69fe406857123ddb1f77406cfe228c0ecc76aa225e987ea9e78a5b8c2)
#   - OpenAgentLib/SystemPlugins/Code/generate_file.py -> generate_file.py:1 (lines: 21, sha256: 772153d59b1cd3e534f64b73af989135103161a350ef363bc8ef58d80a3b9309)
#   - OpenAgentLib/SystemPlugins/Code/generate_mcub_module.py -> generate_mcub_module.py:1 (lines: 21, sha256: e968d453f1488b926deaeefeeccfd22f0a5c3e3a2f959852cb8adb87818ceb17)
#   - OpenAgentLib/SystemPlugins/Code/read_docs.py -> read_docs.py:1 (lines: 21, sha256: 380745151e0c80ee2ad3207456868ee08cd8686a79546139ff4d21955d56c7c9)
#   - OpenAgentLib/SystemPlugins/Context/clear.py -> clear.py:1 (lines: 21, sha256: 3af960fa8a23c2ce9f6b4b6d8c030ca320d12412bac290edde191138268a42a0)
#   - OpenAgentLib/SystemPlugins/Context/discard.py -> discard.py:1 (lines: 21, sha256: e85ddb889751e4fd47a2638ba257fedc11fd1b6daae72d5980264ffea8678d04)
#   - OpenAgentLib/SystemPlugins/Context/media_context.py -> media_context.py:1 (lines: 21, sha256: f745c580dbae1e147a25c880ee69f5151593ced2ff291f01db0740a8aa1a4228)
#   - OpenAgentLib/SystemPlugins/Context/prune.py -> prune.py:1 (lines: 21, sha256: 3787ce15d8bc03ddd0f4eb969cc040f7a90f169af5263963e8b868f7a6645922)
#   - OpenAgentLib/SystemPlugins/Context/regenerate.py -> regenerate.py:1 (lines: 21, sha256: 707d0b737f8c83d44473aa35b241831bf0deca5bf64f37cabb0654f007bd15fc)
#   - OpenAgentLib/SystemPlugins/Context/remember.py -> remember.py:1 (lines: 21, sha256: b7cfd86e118382a47eed196dd849ef7546a8ac0857ad28efe422592237eedfc9)
#   - OpenAgentLib/SystemPlugins/Context/reply_context.py -> reply_context.py:1 (lines: 21, sha256: f6326220f3fb5c846b79f4d88e05fc05dce64a35ede49965be9cbece7a1eca17)
#   - OpenAgentLib/SystemPlugins/Context/tool_output.py -> tool_output.py:1 (lines: 25, sha256: 4024cf3159482299ffb14acc3cb6909bff3b35128445c1512c44d18e9da3f077)
#   - OpenAgentLib/SystemPlugins/SkillsAgent/activate.py -> activate.py:1 (lines: 21, sha256: 81140095ae3ce4971923c6ff9b9791d257694a1a388f46dd2ea5ab30ea5b7922)
#   - OpenAgentLib/SystemPlugins/SkillsAgent/export_md.py -> export_md.py:1 (lines: 21, sha256: 570a69a7a82de9d987c8a07cc6ce8759459b0cdb9f2cde3f16b72e5f92d0d567)
#   - OpenAgentLib/SystemPlugins/SkillsAgent/import_md.py -> import_md.py:1 (lines: 21, sha256: a7acc7c89bbe29793326c61e568412f7e36ec14077c8b529e2341cb0c7ae5d2d)
#   - OpenAgentLib/SystemPlugins/SkillsAgent/install.py -> install.py:1 (lines: 21, sha256: 3f3e3755684099fcd3720713b17241484289d647c87625dbfd416f3c46c51648)
#   - OpenAgentLib/SystemPlugins/SkillsAgent/list.py -> list.py:1 (lines: 21, sha256: 19c378c4b675b36c65447758d3fa96142a809e6d195d3dbbe578041d055c0cb9)
#   - OpenAgentLib/SystemPlugins/SkillsAgent/read.py -> read.py:1 (lines: 21, sha256: 2da1177a8f2b6d960314f6f6b6016b5e2f6d96418411079be594aa8bf1fc61d0)
#   - OpenAgentLib/SystemPlugins/SkillsAgent/repo_list.py -> repo_list.py:1 (lines: 21, sha256: b47211d7700f67ee9929e20aee6993adbe0fa037c1e4d2f505f9a176e61bb50a)
#   - OpenAgentLib/SystemPlugins/SkillsAgent/save.py -> save.py:1 (lines: 22, sha256: 6dde572744a387969354ca584f618d45c76e7b70f1b0384b92e62caf79756a20)
#   - OpenAgentLib/SystemPlugins/SkillsAgent/save_from_ai.py -> save_from_ai.py:1 (lines: 21, sha256: 9b8a067e854f613e0ac8aaa30aad2e15264c9e6e5bfd8c523711d8cdeb660c3f)
#   - OpenAgentLib/SystemPlugins/Thinking/note.py -> note.py:1 (lines: 21, sha256: 41aa63e5db77c5e0629fa8a80306fc559a6685ab7c3f4bd2e6912a3b4c7f8f8a)
#   - OpenAgentLib/SystemPlugins/Todo/add.py -> add.py:1 (lines: 21, sha256: 6a685c9df397f31fb74f627aa33bd621a2041080ecbe3cca36f15ae44b2120cb)
#   - OpenAgentLib/SystemPlugins/Todo/clear.py -> clear.py:1 (lines: 21, sha256: 0bd9409c9bff3ff71d6595e8c08057f1097c43f5589e33e1452d1d185bb3a72c)
#   - OpenAgentLib/SystemPlugins/Todo/close.py -> close.py:1 (lines: 21, sha256: 7804db237a5009e15028efc110adc6174cb4bf9c4b72225f91160e6229f54dd6)
#   - OpenAgentLib/SystemPlugins/Todo/closeall.py -> closeall.py:1 (lines: 21, sha256: d6d9f2cda4336a49db61c650c60e4b417566c01e2a409520672e5c9cfee15f0f)
#   - OpenAgentLib/SystemPlugins/Todo/current.py -> current.py:1 (lines: 21, sha256: 0b7fe171c4d9f69e59d361b5ffb52409e7069d392b72aced749224ca9a8e24bc)
#   - OpenAgentLib/SystemPlugins/Todo/delete.py -> delete.py:1 (lines: 21, sha256: 4862fdfaf5f0ca3e02cc39299f731e5403e0eaedd95a47315731b19b6633d256)
#   - OpenAgentLib/SystemPlugins/Todo/edit.py -> edit.py:1 (lines: 21, sha256: 51ef999af1868bbf05433d28ed61ad16fd7e50ab762de2f43451390e09b6dddd)
#   - OpenAgentLib/SystemPlugins/Utility/agent_log.py -> agent_log.py:1 (lines: 21, sha256: 05a6b2c420c2b4f1c3fff7f8cbf74f92cb0082dfa3c9d0ea2a82919f37a79d89)
#   - OpenAgentLib/SystemPlugins/Utility/error_file.py -> error_file.py:1 (lines: 21, sha256: 7dedf862a0be2509ec1306a7442a7a4683c2e53d229ef37e2f004e1bbb4d5b11)
#   - OpenAgentLib/SystemPlugins/Utility/list_tools.py -> list_tools.py:1 (lines: 21, sha256: 466f57121a88e8a34a5a6889ebf49bfb82f6f58a587f1ef6b8e5267a8632bbf7)
#   - OpenAgentLib/SystemPlugins/Utility/placeholders.py -> placeholders.py:1 (lines: 21, sha256: 79baea2c020fa95f1f0d908adefc606f4b2d0c70252cb97a80f2ebaf04343452)
#   - OpenAgentLib/SystemPlugins/Utility/plugin_docs.py -> plugin_docs.py:1 (lines: 21, sha256: 69d18aad1386c154e2fc72771eb449723c2e1f7f16a6962c4ebc1d4d2767b33a)
#   - OpenAgentLib/SystemPlugins/Utility/random_template.py -> random_template.py:1 (lines: 21, sha256: 12cf31c22bdf39a1c1886463cc7aae7747961b30cef0a61dbaf9f9a1b70ce193)
#   - OpenAgentLib/SystemPlugins/Utility/token_usage.py -> token_usage.py:1 (lines: 21, sha256: a594d4fd7bf9fd7121909b2b3979be19f828216f6d123344efe15232c1f49c80)
#   - OpenAgentLib/SystemPlugins/Utility/tool_help.py -> tool_help.py:1 (lines: 21, sha256: 0bf8943cd63b0d1f5084ec135a934a4f84a5cb5959c74f125d0b0bfd9865af0e)
#   - OpenAgentLib/SystemPlugins/__init__.py -> __init__.py:1 (lines: 16, sha256: 0f7ca2a08fa17665665895689ac20340888a048a537735b0096f9bc7df85636b)
#   - OpenAgentLib/SystemPlugins/base.py -> base.py:1 (lines: 277, sha256: 64b1b27cd8bc0c7f1130bfa6a079ebd75c3f598a99742c9e84a018790e6ef3d9)
#   - OpenAgentLib/TodoService.py -> TodoService.py:1 (lines: 203, sha256: 92683bd65b634974f78b4049f119becb92a3d09e44aacca2b487dd217f906282)
#   - OpenAgentLib/ToolDispatch.py -> ToolDispatch.py:1 (lines: 1152, sha256: aef15cafc8e5d7baf0ed66acaab3b325f5dbde8f6fe99443c4ff5291999b566e)
#   - OpenAgentLib/__init__.py -> __init__.py:1 (lines: 14, sha256: 21fca903f07c84058eb38ea9e71b3c2484a99b1b7166d7caf035623588fe2865)

from __future__ import annotations
# Generated by CubKit. Do not edit this header by hand.
# CubKit repository: https://github.com/hairpin01/CubKit
# CubKit build notes:
# - Metadata comments above were generated/normalized from cubkit.toml and entrypoint code.
# - Bundled helper files are stored below as a base85-encoded zip payload.
# - On import, CubKit verifies the payload SHA256 and extracts it into CUBKIT_CACHE_DIR or ~/.cache/cubkit.
# - CubKit import-debug comments below explain sys.path/package wiring for private relative imports.
# - Vendored libraries declared in [libs] are exposed as `cubkit.lib.<name>`.
__cubkit_module_id__ = 'openagent'
__cubkit_package_dirs__ = ('OpenAgentLib',)
__cubkit_lib_dir__ = '_cubkit_lib'
__cubkit_bundle_sha256__ = '602acffb8794c82d1da0f25cecb6036da664d0cb35fb6d7a95d08fb0876fe995'
__cubkit_bundle_b85__ = """
P)h>@6aWAK2mk;8ApimClK@o$005~7000aC002!xRYFB}Wo~pXaCy~MTWi}e6n^)w5Z*)WkeEIPHkK_L1eR{F4hn4$!ah#5I+Bo-
rTO<ek{n-`uC!0}OJbk%U2K2nB=5-2AIqEBH=ctqFk2NMEH63eIa#l+qf*Nqp|srFy#`7N-zljrVM0jDESJJWp~oH-
7u!>PA&$|h)f`36WfbKVGltOh=U<<`{6Up@MDQq}M1C%~r8F^6l~W@3*2%};6^O+aJL4%aa<6ls;DL^QN-
R9$S7UWbW*^9v6c8BQ;fONoiOBmvIH+|Av88+3?{qTQ;6C~V%?|WzaR<h*EjVU8?bq^(2T|{<J{`2&GfR2V^aNwHzMOR3rhTLVQG
gEEE#Nz{Itd&PpaoP@5-*nP)fHVW@v*w6mJ+F()`rXzc4QFOP}jhwcVMBXJ>c-*%K-
rWA>vx^p?_U*1;yD4hDLc{&r4fI)+g)mh?&b};a<{Zzb+(YMM0U~8fs-
D^p#Zx#u>w+nUjhedy8q@VB_s3@@+o*KH^YtoAjWa08h!pN!7WYOdbx+sfYN0x8sntGZeRxX9vccY0FFnppxN(KDo`9LNd$|z98o
!ZTmFfq>GT+!98eD)$#4$gi#VvZ~Qh2sK7$KFwZ*v$7cMGwOZ1T%s>(+n)(RPdbxRZFM(360x!uuGhz5gs}@(lh$l{4aK}S%I;P0
RMxO28EznokcJP<D^|H@48TRZeYzBgt7_FtBu=-
JHsX*If^XnaQ+}gz;&xiQ<PTYw&`z^Uhdg)IyZ08CUBT89S;a?0~pB{eEj@CuAiT(mmO9KQH000080000X07@>gK(Q160O(Qx03H
AU08embZb4^dZgfm(VlP8)ZggdMbW>$=c4=c}E^v9>9BYr;xbge`3PSx5JCU7D&@1lTbI|mXLxU!_L3Xcb>$rl}qP@D6C0CO7ajy
S+XNGTz@_KVuw5Wk(Wr`fmi^G}W(7$2lAK(0S^gdtkvf-n5886#>ne%$WKD@g)S=QB>CCPHzZfl+-
EMIS`x@BouR&CnmRoR@J$hMlRr#4@6F>;f(S4DoQhJA#u;zfJE$;*{$e_h_6i1tNQ^D&GVLkHfd_it|itCN$HMUgfQJKON`^$J?P
tIC$&wdcIP0rV#)3_ej5LGul-8$xe%l{alw-?J-TY@m^~S82<#iUIyC;{YjRRmnbl_v0T~b@>xtw9ObmoDi(!FR$Ofdy{-
Rd;j*FO&K8gGcu_i?4strY56*eS+s3<jeh|%m?|yXXg?IAzdQTz@%48XZ{H*zKfV3_-
CqF&;I`hRi<W0>Q}dg=+FInWh64=1W+CXBL;}vm+1dN#?8l3bKVBr~AK$%ypZw|F4;KjS`)yIMwyFwNZQIQjAfz_{x~<qUFZe`}A
rX0Z_Cs?1xATj)9{?d}LJ$M$L5%xbwS}1pJ&>=3)&f~3aT~KwJcSvqI9uZ6n>w#*g)j`uSY#mH)_KcWimw-
W!>L<dZu9n@HQV(%1+kDg3f?vZQu9!C<?ObquN|0qdj-U@lJg8T2!~bcyhWC-
0mpR3n=$)Xa}di7pD+{;TUBY%#2{}#19djGA;MHmTc>&1LOb%UL5j;2&z{#nYm7`;17!`Xw`I&)-
k`2G+XDM9wsnm>x;T4t=7Oz&f9#)I=q+YM-UxL@`fk&@1oQ#bH$oTl5_Oy{Q`A7yxG1(6x54HxU%_uuDVLVlV|FHlzbSwSMuGs|U
T4*93A$a}kHzqz(1t%WxNsM14t&h0CF4sbmq{X7IH)Vo9|nAhg>cJuf~z!UMGnlK0A?*{&x@C*r>8?Udd0GQ(axwl{5PLyd<mN=H
Vz~l2Ko|3L){}^g8a(?b{w)-
625+G!N5PW3B8}QXDs?$j>qF!3qo0>ApN;vQq93ym24Lw714y@pO^%V2tWgZ+DmqjP4T!<R`oh9@}GI)^F`0G0EIF%fGwC<JOED3
&D*EuvCBR2F2F<fFZM%Ka>EKROP>T`DJ;9{CeL_1YSJZF!c+Q>9LAw+2@ia|Y44w3!kPur>zoVoW-
*`itjSAUcMCp1Qer}7=t@B{6#*MY17oFhaol(Xwox#BNMbfNaX5xf`DQR27u7AV2afy+jL>)F>)5ut9ui_g3$PK0R4*SLCH0|HJc
WqQ1EuB<6D`^h(a@^V3r4P$Dg7@OA1aqLmWh;yQK^O(OQR|vVi28JgSs&-n_JwPokrXM60l&f1;Ug~J98CDX%cV-
|5yqa>TKwj_`$FlV%8y6?R)}JMeWyU5#|~Qsvyb&MQiXxQOxEptM!`8P=q*P|0)zpDkl6LPUt|&tp%L9lUQ_((+%$a1JiZrldigi
$u~L}OSw2a82Sn$fgUhB@P4gm?XfiSZCKE;yBI*naN>sS&Cy~9^YCZRH?*;q{1$gR+CvExyS;)95`7okUUB~gPl4Y7Kzx?o1G+GB
fA@`zgBSaD%1(ppZ8ksA&5mBoTtR~xI1RS84RC=TR-vIYK=$b9k~7QPHyeGL7N7*Uw#@H(*60+ws-Blsb`LEEwpmYk-
L%fD*{OpQb(jew3{b&VN>`N}5cyWw#5owlv~C-8ss;}FWQKhQR`>9>20<8-
K=9|z%MLBG7ZZyqgaEuhwag$d6I3~=CH6a#SDEoU6j+T;+5nvgoC8#wy@=U}{&@%jU$D!JhRz-CkP+(|2_K1Puw8dL0a(A^tEsp4
I)iMY37=q(OK?4}4VSL@2Ky5cG<af|yiV_wRwJ|E>%d)RPucHc<~P0UcwjgOdSEs@7k!BZ{+W%OZU!5r_fLgV#Ox_{pC7P#&8EoP
q$;umG&HF>1fmknUuFZZ!HR_qV7uKEd=?xXgy~wxbHrEsTusFU$~0diq9S83W9h?FsDgnS?SHNl_CIXl3=hdz<Gy`_(KD}O#{ep|
M{NsjyI-*KEii}Izh!@ZWh-
!aF^6r0rJDzqe=l2S6Pgs%)oN3A;XstPD0o^X?Nwf0gF+@CO7K73uX0sc5s2{_+|W*~bcX=tduun_)mV2f;RX(gNB%fVACCxIAr!
8g!9l}7WaPGkF9`rwg;XgVHpCb+413nm0nC;tm{u=J_?j5^=m<>V$zZy{P1<!4^m>RjTD;t@c@43!0v|JfA@m1qn8_-
y%j&j_hOU8lD6kS7avcK1S9#CNXtpCv_j9(xx%QLK<xY;?M;$*I0{hQpH2$f|%K-
s$VkgDIM7TAHh(5?g@A6Ga82$I&EZ89_VtAcU+)}1%KG07TfpzD@SHP#5kDKk~ppIt$NJl@v9{v4v^i47z&7UE!MiGhGz@oSmzX2
De_D7>}moM0NHu?H=ZU!9KRi*wlo4hD^CTLisMbWdTKJ~&$O{5ijwr$-
cb$aWyqf_EFiEO0Th^e&%6T%b91KW`<zsdQnSj7Hb?eJH?O{}Dn%zJioN)FIKq#@s9GGV5kv%E<!3n!Jt3+WwMQx6fG3m^QcKJeB
+3u?pr`n!I(NA+yt%sU^~zPVH%ogiE1Syt#A>F<SuBH5NV6qjQ%7sI;rvby1O7zFDt0MN!`<O*#*E<%WObl4?s8C{@D^zBZo-
2N3qC7t*PEF;ps3EOEcM43MsJ=u4=3WeNJ;L+Pjs%ZDcY)7$AIO)D;JFUk1d0?>3U8&DIUwyg*pIlTRh-SkVAd@yG9<Xnv%RVOVN
SHYBGy)MtuNX#cAUqHvwvN$kKJoDRD5Qi2R|;%zW*+JjmBc?%`H<h`W$-{n1ro7ki(}#1uK5~0VvIAP(=uPFLl<+Rf|e;!p-
3anZH(<cc(8*XIRaJ*>_DgqG!~4i4>M8uOfa_O!}wvlmGP8A;=bv<E!5!9)8AVIV)N<4k8)kq)ZMg1v*BCK={O-
N(o0_Sr421Z&Wm)@fQ!zSMU}RpEFgX!a{sz%!~QL{hW#GhT)y5E=!bM%!+?hk<Ak<IXT&B__!eD*Sc`FJa>`ZX4N8Dn>9%OSfy3D
ODw#8tf8CcZPp0nI*j_-EaGFh3HvIoxIyRNZi^m@I-
;q!6L5{E>k2vo#tnNGXa=7kWyWvr%1~%#@Zw_Xo$V;AJ?nQ(=+IEH_8%zbAVg^F^$BrZq00ps9QXK_}d2A08xs{P;nPj=L!FU>(<
e6ZV6*;1>XE38)8xb&5I03lHkwXdu<ri|1ShOmt%e3g6>>*4+QiA8h%?8OpQ~<_varBz5D2-
$gZX$T4r$0zkT~$^@;S%tRFtBD7GikS6cImSl0p>pJuxmxutpR!fXYe|3-
<GE?JwjGO>JA*QudxGg6((z@7xfmjna%`~>YBb<86J$MWR%pmJo;iT0|o0#VEbHeDC^P=@cS758w|k{f8iVmp=$))44KctE!t@a`
_WG0v>&&3)`229RaC-2ZreaFP+l%7Oz2IcZMz(O-
Hp^}BpAJ_xIu5g2wetcM(QFhKpgm0MgL1;weBuLPOTrA{7*RVJMrW=wd%>3HCMHJEUDunT4Pn-6TNt31Vw-
5eJ}xv{Y=`kt?%7lI)u=O^;iQb``E}iCfL?V<=q04@@MC7>l%<u8*K3%R+yovR%2OnGFV2Yw#O+RLL}HS1?)iGb^vJa?a|K0cJM$
Hu~f&QhFL@F=*c-
3vqI^q+P2ntIe7WiDQ#d{8qc4zm))b)K2!2=5`^TVm^(FWb~<Rao$4pI18VCO|8tuKU#H?v99Ds;esViFOqn|0!VZpYw!u^+X}#(
*DRMcw?u&hJ;@b%6v01qp{8-K`$SPlN*UC>iwcez6_8WAdoT3-
UZ|SU*o3z++Y30#fAk4{u0VHFEm(H6FI}2lQalhfTHe&V{1V+!p@GKHs$c>T&3azC6u_Dd!kkGMioL!$}dxVeFsrNxI#7p{G{t-
m|7{|Ip^f0G#;ej1}c=D*B<QyrQ@w0${KhIJVo**^zZnhc+(%}ux(m9{O)-
ibvV2ZnkB4!fk)FOVJF8Cp%ij&cUoNQd98##!c(*90fChgF9li=bDB+t6VL59YVK@8Og(K)Oh7UQa#7U}vjOPNT55)PPkMxUom*6
5RX5hXehU0v!~)$om69N!D<^B?*(PeGDCy8h}GP^nz?=jch)VVFjyfB)!PD%#U@^zwjvDm2n^xH?J$gO$ThSPemmHt-
S;<pPypY8YxrdI?as5G{L3Nm#-%3TAANS#~{(Sp+^vk{ca6--I^{Q)?`q8?0S4Ef&a8Ft2#h%gxLggwwIglGAuxZFtpXzugsHgS>
N6=K;>twbaswIbf$ls|`(unnN$>;4szA=+zQjfy;Dpts)XnN3hk`4QI&1*n#)4xT3O*rm9=+SuM*rIdHvH$WfLf_He<3Ef>L9z&F
-5iqM;#&XGQaENKIgLH*O_zFa7ilxB`v*L(#k1Wq6}exbV&h)J4iTZ50zZ&V)UxNMhNPRdl!_(Zl2Y@l|{fwpz7aEz-FA-_FO7=3
Ni0k!U6hdev@8in5NfQ;!Jhnpv1Kc$VffQfc_EbEuu;-
0v3CW>A}uI@xFD2?BC&znw@)v)*DZ7;caoWZw;;ISL^cUnm`RW`F{dsGtD?pBC-(g#4x8*rh->Ui=)r7u*NC}~-
3%WMp`qG_zt7$$DDTyd+)C#JBGh?okdj-MQe3gxM$OdjAu!>oXxY={|0%h*h#nr{l2C3;jar~=gJdkXXLstC^2rBelf#*|eV?<yO
%%F^m9fODYEn_|J>F0P^#0t;$OJ%LbBAFpDIsg=~Jmdl182TXJYXf7mM5d>veRbCWc5m0l5mnh`j0|9D6wo+n1`sf_(3en0t2{7{
e6uKA*7502B$l%a~BawWj2?hH^Ry69J&ACZ|H7y9vQjpHMbAUiLQPe$S^0vhn&2NAhMD##Z7Tz_w%ji6yh;-
W8%>rFiZCW^|tm1gJ+w%i(9J(Om_rI5j!FTZhEn-
!`yf!d_ayYfLG*r9%lyp6tvL~NQb2()KQ;g_TH*}~=2f2vcRH#HOzo0(GU_t5?fFuEsNfBtz%~`Kr)H^Z#9*=@|g#SKrB8oL%U-
Dm;a{SNUOQ3O&KJ#)-xN_sAHy~>ktrHNLg`ztcRPYhaLsrt_j<}bn><w7H1W&$U_mQvMa}1;9vPg8Qug|H9S+gYdEsMS+mVaMF-
M3J84h)-zKE`9O-
tNF8p~^sanLF<Si$W5s;&X|v6^%I+$W#AV$_RxzMDs2+R+V!f9nKXBT?Xesc9!u&7ZQ3IX(cz*CbV5#X?>7?hhC=!9PDgc@Fd-
~75Vzz5oWzQ#e<++4`h)J-|P6bR)tOZ10uER1hrUUTMyigIZB)Xm-
3;Ns8z=GT^*DTpBI~B*7$JYd4GNB1INHl?P}n(sHcSVSd{wf0ebW0hl^H+PASiq*JFk(T@SQjClZxiMR2F^&6f#Y3%0}T$8BtMr_
$frHhJP^#EGs;u(}T|F6`649@Hv}8J&@alNPS~D5p6L*W%(MrqFLRYk!4Z&xh6B{@N>u<F2YAd&qiNRH-
6`7hkI?1@YvwN#UXDQIhbAL#waRIEF*kr3i6Y<&5boxCjtp00A{GiISJ0VAY)fZ_22h&BK<i&UD@l4;{82arwrQsh^lq_=j>#QVJ
Hj$1qnP$V%QC1$oL|#+JT3W50ETu2d~A(WO=tAGT-
~Zk_8;4m@=)O2h}=UgFN{d>7ZGWR0vvq`Eidn{B)}KJVND(ihpSpPew5*_CMfZ0Ft;nw$N>kA^NT^mgByxx%L|>Q^m9F>3GcS&Z3
*^BWJhxr~SChaS2W#{@cEwh;W>SKC_MDUDU(tG=Hq)*{_bYxpL`D-gv!)x(B?LZIYGY2WSUrC=={x)<-->Y6|7`dGp-gFuSkNc;7
Tt;n6k5LL5_y@@W-i0YyowE&-Lh$6*LkgV$JpZGV!n`oS0<MW;D2<)n(z`>gOA&x0aZ_`{lgh|?5Ct?<Xdz-
^P(sSe{QS0gr@hIqjsgK-SdxmOGCDjeDYnWte+PY)h{2^spG}|!SvZ|^T>iHvBAclnL{x4GICvor-
^cQ48@GbqpmH6oT5cSJ0*46GK3Pe1cZWugJkB5JYLH7C*cf}48JuBL8_>@^aWcnWW(>>uE6q2slh*F!Ad9RVd&(psB{BY#yGo%x1
p)2Uujfm2H3T|a!K~#iqImtw|zUB0}p^Hr{5~CiFEddS*)=DedPC$S4szlnZTm4EJ)UP~u(9TQt?BmX_%;-
Mmh7I1R!A!r;PRjlUa%@(D&o4F(g&}?^pIw*txI|YtI<Prr!U9@M;kZCIp;EZ1c3WEnnjI<QyMs{WWsv~fal>0#iQ@zqc$awSjW>
4;tujO~O*p-6n^2y3bMYvJqK@d13tf8Ys*(ZK%@#?dFqvi_eRM5$#?^J1*<_?4&U==n6;t<Tf1D-
yAJq)z++DZxinbIHcE9*6H3^s0M4g2eeG>QVt-D5OX2nf6d0*6lw2Ve<hn0h#e~0x!*o@8;Aut<#fle^%M-
S|j$Yt8_WLp<fTuxRYC@9BC5q?^@YDQjnay`r~Yz}KZsW|oZ3w5Lki=KB&l?mV<U!T8Ce*E<Qe5P=jJ7WxSX}zNIM@gJKpr@bbJD
ly&1I6*X-W&|*yu3*ZDkVt-fypApas)Y*O2N2i0AZsDed(NA7*>#DRwY<2v27BN=1+MO?E@}QV)t988>&;Dy7e6Woe5dLdk7cMsi
Sc5`#pqCr@w=dpFaZ|tJqA{j2@R`Q4>kE7XcpISz{Q25i9lg9Fty=!Wg58meY-
=(6TG)#z~T3F?6C`xhQ;5Q95o>&xJgAJwN$3P)h>@6aWAK2mk;8ApnYRR#t5b005UF000>P002*LWo|)dWo~p#X<{!-
X=Y_(d1Gv4E^v9JTI-J6#ufg*Pccw_WEa?#sQU$41$Hi|0Xs3`?F}n~7?C4svg8cI8G5a53^+-Frl^~XW3&MhBWckzZQ&n5n-p%-
ra+%SdWC&~`Vo3&co9ia(mGkgSd#Od%beSsnb~L1jq5M`<lri`2ovPsicOfLV@muUx_0GgXY6wqndUf<flo{mQP<<XM3^xyv80@d
oe<+;Id$kL23&{Nofs@;%%VKR$(cvlB!*pLvxvTY-
3ca?MZYd%L1N4+9$}XzpjJ2(!LMP4C&Vw`AVPo|F*tgSMt62B2MdABgvV7nCf3Yy$TfPKvfd7YpHiume6EZ*mqPm3Lk^!%s|<rX8
l`7}Y%)finGVPHt{~2M4;>89%bbyrl?I+-
Dv=00;_vR2WAI)w4lHosNP!N~S@Kcq;raX)wTWNqp%Mp;F)i(95!j>V37IKCe#qrEaf$}4KuGSIBQU8M_=ONL6Oy<l$ag&nfZfcn
hWwNV2>WE|4Mdp$Wf4Y4#32(OyC@LEA8}bmKOl~W<do<y$fiEAq%$j{QZZi_&lEQgP@2l&7Ix4n_fLd}Edt+s9!#c465pi^hAi&7
nArlIP6<Pd5S!TLEc3nG6k&eg5Uj!&CTNt~dGq1hrsOA(1Tb8!8Afj0Cs=R>p=*-
y7$QykXgtnaQc{=jK#f*Ac^0vIO)v*%3}$O$sq~UcW^+a1aIz-E!N?&tK#u%?tV4kVJ;kQJ4zSd$o>%OYj7&kWZ%sD~OX1dubFE-
xg4bc_CG3bi2R*!wRuE>JE+jCduGp+e8oHLB1wNC+w5C{YVV6QC+-
k)bi0_Lr17O0dnoncP;sKKoaNOC#Ee%ch<zq!F?&_N7LTYZ&F9%-7)Fn2>rpk-aOcI6Yn1*4f|9Os_NpgFe*a!p}80OeIE|A=i^=
fUo7{e4Ersj(<_tq+zf}arLCHk!RdljFl5#1FD+C?sLxj##3UX%uDB!vo~<!@rAB*&9$77K<o%OWOa4rL^RZ>`$GC&GiJo0wCAqx
Gggf~tG+dcY+a^f8+HWPCU*$w{wL0To`O&r$oZWmJu7yW8znyNyQOXd1QdurxUT=%4?4{9eC;2dED#CufsEvPkqR(U%@t$Fy0mH9
PHE8+g}it$MT3&`jU^o92l6#2uUw2YZ6pcltm!5JPr;_xGqD49?<;dZ%)xmp=dmK%<6H--
0iLvwYnKh#nZSH_&(ZH)Lz)(J(sQZllxa7@bC|)@W86Fpnpn-hZ4i4P}W<!nslA1u_b&aDw{@80vKn4PWwbP^&*0Na)9$eq{s`>(
jxReqF+-Mn#-
dxTux6m*cI&NLQPXF>qVP1h8GcA#&S;^;d=XKueoab^<omk}_oZ_0cD<2SiBI!K1KS*%WK_X06lewA!_9z18e?z?|_Eo_zZLJLh+
Qeg5d<WDd&8{p2}*h$nbmw>HZeuj&<L#Dx@7YIT}M*QmETM!S|$?EK-
q3u<(UiBssZ*J>2o)KndU11rkYWNEEiYqqN`$f{Nsl1c~SNAHG#xHfNeR)OC=pLo#f3EhjuhAEfJD?x#>QL$DdNR39P*#=iO+K}g
<nV~g$@bip`R4kwQ5Leud128qT8j>p(Q}Jt40oIzWv)a1IHC5SM4d3-qAN%{ky*HL=bQZ1BYW>%<H>c8d?w~XEDG-
@&I_0A8YN3geIVxL<(Xv!6r9DVV+Y|uJw$W`gTlIFmTkABd+T5S(lKS7zRJnK+(%kN;dXW@L^#uY#|2B2~h!qGU1Bl{U+KUR!wi2
7M<%J@pUNwwH71FEPtu~Byv)R(B|2bPk&(wl^i^^H-
wj|3g<h%8DtJPc8PF+==w$X$*4HM@t8R1v?1nI^t5t~>7wv1XM5u0Fpyrv^Vt=382AD%yaFl2H2e)#0m-
+Vq~(1F9#z4wP~OdSG`AO3O3R8tL)U;Gsw!<HD{?mrqb=-
)sic=_#HL#Eok!)4tBEGX#fJv@B=_;*7FRUzW~!5;t*{STN~s8^7zyIO@k|Kv|YCQhj1sG%=DQ%GA8eeozHf>>5>-
ws(IsRK?@>;V?-d-dDK)J-=p1v{|}HnF&BPuEq@1Wa8ji}pw{Q0>KLIvbTI=AX>Joqsj|dj8Gg9-
4o>_~qgQH2?SfYc&6A@%H>*^DpP$%)czJt=pr(afoIF>9exl=rRZ1_W`PuKQ0|bgivWq`yl;6C}i<&{NY1T1;j7z&L1!CF5V6YZm
w9z=Bq&k{g|y{3Mht59W5LV1`xKE!=bG@JUBSW>j(C-
$do$}BBJQT0G0@DUa0TSAk(gGulA*3SZ&$*g%~j0WCD9>6~#(H97w)$tf8Q$Rv<d~m`dph$ax>1mM2tBgONI+(AqIshE~5a#nksG
GpZFucW~|bA6`CyqIOboF=dscv8{w^6vi>I8&luK+qW>Q@OV0E^A)(;*?*_z0Gjw(r`@i%yU-
{^&A~gm#yt;~pe!KIt?zSnm8`a*S8sM2%}%|oHvz!mea+zrRP2Qd;T^qhB+a|{-qqQtcN@@f!4{<1s&yK*Q10Ku>O30!7%Ch(1-
GCPQAb1`q#v=PrD{vF)P%OAR;wGWW?OG*?j~EBu(IF6PCzbR)iXYt5wWZ(_ZPpK{|D;IH;~GY7jG@@ZKr2^N&XPZ&*Due1piq40&
2sX7l@GL+$XbRy^}m?v?`L8M2GR|C2_{(6XG-ClqW>0unZg$GM?yz&oaX<*-
s8Lm&coQjHsXtN)WTiZi=~Lw3{z{d;16;_j;LGq==651UEs)<CSAXwFHzE#7iBt#y^n08h|L<%(@KA1eJO@DPRK=TPx-
!0vWL_Rv9PQxbcQbXd{Ae!A}nT88PFbU7%VuTXHnKpBxSE?d=u$@OX(;wn`*|`pah)iogEqD?hsO!i%roK*SLw;heAyb#yRn*y4>
FRzYHvjT|Pb$~Ik24R#LPxkXY#DWi$-oL-pf-T+9{eL)ykW^(QulI)>Mq}W8CRz-
v*^*MeizXlCxPVHzcI_XksW$y;EXWSWmvN;7U2EY$BQ+Un}>g|&WE|M`smvASGiXy{QITM2&?2c^Qi<Au`Ww*r0X*@-
ZF6GX#<1yXJgaU88c;m*ES6()+Ub%MVXo=p-dnlS=?4O){;&+iF)15Ynsn-
!_QN@xW!pV4>_z;w1kU9zLAsyqC$$iL1A&<dwH&vXU-N_MIs{TL+W`n_5)aVLj?vO_7A$Rju@(G|J2xjWiMnuv8zn^-
##Ad}J!=oH>3*z)?N#p5%4;E367v17KEwvvowNj|#PB$-
nv!O@WI+?_~Ms*O0#Yu)dy8kO5!NBo)_4VzZ88Bt}n2GXMA$gJSqO;Ga`Bm!}G_OU9yrge4i&S|AT_^s5+A1N4L*f&ruAg{#D+Of
`g))*;5w*6sNO1V=IQ;Y=@KUTU2U2oY)-FZR&q;x(;(&B>t!}&|!8YPhn7NSZRum)1e-v%v%DL%r99CjwAGHThWrCVXkxf^-
f$dfq0Zp-ov~+!>Xa-8b)eFq@S*E&W%QYvN!^?v4^r2;Tcy(g1%h4z2kmuHv^uicjPAZPp<C{g4QHZ$MGhrvtQ)u*tzQzR-
^=k`JBr_{+3y1t(|Duvt=$>A9m|7X9=PuPZWu!V2$k3{_dIQ0#O9~wk-8t(CLe&MVs_qcU8>f<@%ILH)0}5THDYlwE)-
0x%0qiP52C$dj%)q8X@BNnc&n!MVrBtoU<5Gn!)s2VPc$MCSNhODn+=oov$T7P6-!5A>^-
i&(ad!mOZp?Q}%fAv(l(7BX+u1QqAU4gUe}8t}Uu8VIb93kaP)h>@6aWAK2mk;8Apol2ZjLen005x{001EX002*LWo|)dWo~p#X<
{!;VQyh(WpXc1K~rUOb7^mGE^v8;RKbedFc7`_D+c$lHaMZ@fXfzoS!lO~?4b~X5!N^nm8D=QT}s=3?~JrkVkb}^Vrlf=^Jv~o-
of_Ur|+xJsz>8+^(4`FH7J}m@a5^H7$!SH*9~WXp0MjcjVC*K5XM+9yt2kch!kG*S~!O;VREPe($lgi9&@M&zwq_r7M&xNO#$?jW
w}-6pb?B1Q9^IcPn=x%4*27QLc*)^M`b|33u-
(}Vub!E{F<miLdgv{KZP}mTy_lW_*fYq1El9scEWF9&{o9g`6TZ|M@my1&}~2~=XX-|en-
L$tMB*F#v4`=2XWTE8$|Ez^s8lX9R;jJ9g=}R@N5kdhhO24Z}fvM-ceEWH(2>U!huXj;BCh#RSxw~!|DU@F4mNv3CTSJzjGiITgj
3VBF0+DW`4w#ONYE(9KV$^A>Ou2P%dxA<;Vhhsd<84A`56Tf`Gw=N_iY>80-YRB6Fia!hsq<Ic1y|rpJJ8LUro>Qkfk}-
w&GwVD3^GZ3-n{&yVU0@o)6#F|_-L{%B=3jpruX)@zy(>dcTA+gIknC~sUOa5YOz$(DMhlIsKdid}7Jkm`D#J-
c`f3l0<T8DGO>+z{SOZE0E(C)wV>`x|t&whcp*DVHX=!@9UUXI=Hf9age73_+sgzNmp(VYgp$*w5?xN4EpGj4z(XIce@{%M*F0-
IC&>JyIUrfSI_al{!_|y+>2rbwX?UZ*5^0!VlT~hhks+15ir?1QY-O00;m803iU353}}U8vp=Fga7~^0000_aAj^mXJu}5Ole{-
O<`_fXJv9PQ)P2=X>V>WaCz-
L%Z}VucKiMcnt>s5TwT+C%_KFVFpeVwPHfq*gdjn=L9?rFchk)x%OtB?osNJ(Hd$nmWj2{F$R@}t4<L*A0{Iu_OLES+?+00|mNX+
6DM0Ef@;=Tv_q^}n<)1`Pzy6EAIsT$tvASc&pRZZnm**vG7txoWKRY^an@yDG=evH_vOJH<&9-
U#sHp3vFZ!~nyQ3p<t!47t_gz!V?|r#Z*LS;eEx%v(n@WB!y4!kHHmVETY|qO|bz2ubGly9<b<dvnRe8q2+ZO#L{E)DH4L|vf{&r
i|7xH>?6v5|{`gTTNJ}s)MIIGy~C_UoM=U;vDlyw~-CA+8#M@RY7$4{Sr{?(KG>u(-
^_V}B}Pd<J8G|D3A_;*OSKDmpF?kb)|F@jgtJBHtDb`!sV@sCzj(RES&)t1$tTmXs1xZRiK^RiwLKye&DDK=~kvqqh`J&RVC4J-
}dShK1Fy00S`VvT5R0p@Mr&7t2B4X|eCQ7(JtNWr9I)p;5nKO&;=Y4FoBSk5}ayK~VY-xPIm!P>bs03VpvhYw#h#ahjwhkw%4Ob-
tbeF5zN(zYwR9#E1!A|mv<?5+rG*`c^8%03JZPMD+~99?nEroizv2SEeSH#B{eoR=*-
26`T!H|+)MqwBJWRxJZw%X?VKbSi)di3E^9gEg0s5n#B6MW2`JMO4=PEUICV7g5)@(ccriz(x3n;8zT1A@M1J6%{}|)?G?mh#5A;
6^j70V%3+|ECO8QY!>`u3vR+I`f?ymq-f^XjMg`7*Rg1|Yg-VA2!y`Br7?dMHT@-PZ%VuyM13-
Du&@s3gBW5{PQ?*4N3kI=#6rk5G8SaUkwMW#@|5RM&DfevU#I|tVrUl+x@<{D0F4UdVySRB4I)!jhUfw+1r0NcI?#?F*1$Tf>yJT
{y8a+EYybmTuo|XYDMa(C+?4$gCZ5#)6=U0|=%Y;oqAwNq7oUSc)98S563A@ZT}`V}t(k*I5CI7rhbaJj-
|SYdu!vs^%{>9ogVVXA@y?dYpTM~a0=fWVYO}Hs+NmaDh!M?MQr{}&@T1sOeU8FssBIW<2_T(%)8DBJw6agw4IvfJ?CURo`|^KZ{
>P91^zy%=AOG>?zyJ6TdmFs`&zJx0HUe%w4vfx8(6_)MT@oAGlCX$V-
TFlUW0dhOFLr%H&BwXntZ6Eb26#~}`y9yD!5VZaX@7MYhmJr#<2WTyw@C_%&Osj_zO_87OSaxsOv8B}?nRB(^v<L{{=ECbqA^ERn
_KP>lB!_WU>(5kXaJ}A3N%vQH2{~@y(%_m>tdn$fk%e!D)(9w4p0a+PCQ`MR1N358hdDB$&)M2T(&ZsCLQ9Hn1W(ZQ1&T1Zbe~HU
l&ogWq!qO6*S^^lDZ2hZj25_DnI8gD2!;ROf(ZExbU3+Y_7G3gz2y$Q6p}f3S=qDU@Y(o+SqOym=Z{y=<XB~)IIv#ajIm%8{-
Tt@Rf_NIq)db(B!&YgWZrMloyPdG<=rY&`iV|#52({GiP5eJ~%l!)q_d8!Ej3puscq#MHF|p;9zfL+<_#3i^6<2b#)6SySwCpSP#
JtARPU$YkJnv*X^!e^*ajW&|ZSu6+v_{k6+9NrlYm7CgYGB9ZuD^zP<HUT+tBNBZ(UbW{MIA#BXi0>-q2(ZSw>EU4tR-
7^ArAxoC*KVVwH>K?nk+3|~D5M?U9s<SPIZ5QT^@kub~@foGEG;ZpG&4EPnOki5BOZ3_*v4?nP3iB%>h$g>wsbAc3^3>EK?cmTK)
b<7{rVN3RW#en4=(;r&N4zJn$Xy&T9n6KH{?jng*B)ZV?1n}rFS(5VtVn0x8?{+|O7%Cl;3W;IM=H2crY2)R$?YH&md$?E;{D*?d
+i(LVr8ADc`!;^?yMO!L|NQ<p|N8si{B}P3)#9DwJWhv4{<c%2(!F%K_{B%3p0o?OR+GLa1!@`Fj1TYK+%#)eDFs2l6u+fLYrH$b
v*X|bhvZdp#wuZYFdNeK#b&#R&LKeNUNBH$F)Vs()JZavGRH7n4U(vD=^#&q2xDsfzF8Ny<_vXn1NIt!8Ve)Z^xkz=^#$BX_%O%V
5If&?=9=<W53}eb2#u|9$swiT;?y4mME3ougWLjbSUWJ#!|0b&$3b*pB^zK~{F>1KdPva`hy&fuk%me9?t1?2X8!Kq#wJs&Dpu6H
tzwR{-tPLr90)*Ku{yEYpSp0*3Oq@m=*K~lYIf}l5=0*MCB9+_j%?cy&}|v_)9~wJq~8+mp9-
^1;r}{Er#w0_Ty2p2<Bw0YsX?y;of~vI5ZHk73(hs)f?r8`pOO^@nK85CbRn}4jIFN9ntOp58t*VTq~RBsZVco@Y*EEgg+qfG(mD
S3QIfjaB1kIgd<wmtNQrKPbvB`K!X1GDG?KxaeIIdxoA}4=saIt|x@b=9YDGde>;pXOaX+EsdEjMTl{Kd2TJAU_{WX2<wFppKuYr
@}=$h&pb4%dN07^ajKA_ZZxeH5k;@3?#KT`dkv5NJVP5q#YKBpEi3dB_NRaLI80E-
`XWefgV0XC;T<|!>c=sbGbfZ4zR=B!w0AC#|Sv~I{svFF>SW6^it36#G3E?UEYtG>EL&H}?+RT1{bJSKT-
*!_W_CXuj2ke}m!QFHb^^p4ILAi|=H@){EzyY1X0gsCgUyaWt-Xh=1XJaVgpicWN}1hMFQ;oosy<v}&)IQ+{g;tt4{7Zwiw#}N|F
v^1I&PqRHh%exFYNaD5y+6Gr|O-
7$Xh#{s8rOZ#c@bRube8!LiV6MbgL&BQ|eAk<@zcltWz}?wyfseXG8Q?%Ci)h@x<P!t}pFIQ{C!Dy7xETtvg-
C(5dc%RXD27sWmc|pgqjIfdQ7fB7x?knhWG|F9iiCXI+U4Yo#p#UpmFBEl6<ZPbtA<Sh%i4f=iPcS!scj3Qf^V5R8O~KYyiv4Q6c
@(7|CfJ`jW~XeNM;7c=+UDGYjqbMr475C+1ZzcvX>kjMsGaRhL{c|pJ%sS3!R>N{5u}TtF@UITilyU&f_~yj~CIyvqyIb-
;0MoKYK(iAC`~qU<|lWK8mLVJBJNDxcm=j;YcGtNK<!u>Ck>#$Mf%-
vQB7L(;cV^h|+Pd2T0W6mQqoJLjawIIKJO)E4Jh=0scqnc1&`fhK&&cknm_4lwRH4V1U|RmNi)5i@e5|J>~mnsQ8_IhD#W|X>Xn6
wVi$%+doi@tTPVosv{RJZFvFLfIUZPX^Z-TCFp4C1m$t`{wzACe~z?JdMHzKEoqojm+QRT&^sVriuQp}TW-
ACl0bwU%on9j*3<=p@?kW@#Q8!gF-a~^>DQWCoOr`j;-j(a+$9%YJoTDVMnbfnno_d>Mgln_Ornzf*ts?Q2&r;;8YLl-MpSSa=wh
4I!4fY|Q_gdqoH~}sHbME>uJ6P9UemmDl2rN+?w^{Q63tDwaBrhU(yIZMzPZVf+=ioIIpI;<al;9&x9cywb{n+EwjysBhAL>A$V_
0RgI2wFqsHlhYn&dWFYF<aj#8s@YyRi7WOMFxCp0Ccc4jj60S8H^N`RHxi!L(~__GwX>}|!ec-xi$CwP}8+n5vjk)fI$+`z=+ZQt
?|`8b!E+do!^oU%+ecEsbi-B!hlUE<DTn+;54Gzrb7IWE&*13=l-@f(2oFEWv}8VY^YE*}-
P*wW;HriuS%)&X;<pfS41i=jH)dqwOi-^yj-
B}j)Zi&7QCP7Wwfr8QFAoI=BBdokk+tk%L7^`IrO$<B2?pt^6VRo7g1A&elB+JfF>;VxX4NE!}}yKkLroA_pU9wIK>L7K|(qWQh~
-JI^N<aQ3=9)=HW=G!c2BfZ81k4s}gQ*qBWs56g&B${h<^DJ@=vBh4fTDD=EGjJM$aH+eJT)b#-
7_y*^<gOLM<yYHXHaBjdZ)Ny2ibh^eU9(&;b@gZZYf-
Vb4-}8-7QEty(`G>>5zyqbqLM;AR7^7|=)tUuiju-<4X+RAOoE!~FfNPE%m~HY({&R__e%2cybcXK=ffs6?~G5M5e+P`EK-FtZ02
U9om>?dc<73;X<Ka|hhz-O)}<N>u?1ke97FT$S-
WF?_~2|e5UhK%;`qU`5X8r*7io7jR&$Ap5jzH>dJtVE@)`XmHy#GT4s%ffDk?`(Uw24)fo<$}U5+@j*2u&2o;E7(UL1b%U0q^4vg
z#g7_*C<@?ir-WDdt=JRHiFAvMEyXmy-`$XggnB|-=WRmkZ8Kz)_{*~v-
x=C)`%M!Ta~jC>I=1^8*%wz>tipE)VlSl*BkRLCBOB4i+UI10XZ0v11F`8FNj21rhP4iEAGrv!$qgqLCj$)ETm2XRg~Q}KP@X4hv
Q`xA%_TiNv)Z~3@wn?UBmpBVWN0y+BWH5VM@)iF8owyps*%yDMS<3kNgB6X+H4z~zEgM^AaG`WrTT;Fg-Be`Ato%yWhLvioL?*v=
gu=9!&tgXleCFEAyfMR_m7)%4f9h5+RCZJ#^RgG{Y2P;R!CYi3OMLN(X74A_D)sLK)HM9uG!-#^VeOj)A%$-
{Nyb^ahd>N`(a*g{CYnlu3iVV4@z{j3@3!&OD0&mvlw*?mI|8-
IA7^xb*9U~`&FmY4DV$>H7j>7omL)K3ix@drc(zFE3$aIt8;pwh37pBlkzZqE_U*!Y5EBa6$?ZJn#QGuOw98T0RU??_J*a{umTUX
%xx(Xb^O>qi_q7g=GPUKE>hEYR8?U$-%!H8SL-Wf@oTLKL~DOD`nx;r9+kG^F5=@8k^wv_}6PmuF6i_|xrrnH5kC(B}}skuuZs2v
g&7qNiO%)h37#qvPx|C3*DcT##JX>88>?2tKCfcS?})lS?wP}}#`a1>{d12`(2KmDWdl-jbI!UTLCQ3X1o$a^Xunr_6zCFHZ`Dzx
R8_f5-k@ldCz1GmG!V0o6<RNH%P>4ayN_Y<xTOM^Vep0m}iSCC2rWa4C%u8yK*=ZwPnA+c7(NjeX-tExPB2W)q-
y4)b+h&{S>x$4yhycwqM*#tB)O7|+%vymRI(c4#mC!Q2o1lKh-C;?53UrsxNF3`^S<+L-
2vZrwHfbu`9{L~>#8a;|WbP7+$DoqC|>_`7*vFT!9S*}i(CMu4cV1em}C-
ycw6`2l{m<|HRD@<J#=GQxNJzI#}ZH}7l4_{10^P|5ZfRI&HKiNX5N!3lSv6@QJ{wG~5rP)|U-
}lh`+@?5Me!A)&tm1gJ5{)S}Aor5UKc-
l{ff|ot5PYsZ>y<k+VRzW54jD+w(KgPmR+{*dwWE8#CcnL=4dAeNzG+0udNP{E>bxF|tqn~;^zACY0qK%ddh3gDKnl&Jda<|@LjS
_)F=1zUgxX=o8`yW=w(LAtC)*5CJ={J(uK+_z&2}K!_HXbXgd-L<O+*ix{-H2CWS?Fe-
`BKJKVXgnF}<~s?)b8v!E^KWzSE$x7>?#TB!U0``R_^j?^mu(c!TL|YOk5xO+@$^D34*or^I}-tMTc0OjNk1YDGI-
H9jc!%xE_XkB$OMV3*n3iL6lcXS44;^P?*1B~nr%^f%%%odVFU%q)T7q3SGvow_oU1*uc;uM=ZN2bsg5#xBe0ZBHBL;nbOxga~BN
#HOI?Y25@;DtF#!=L4b+*TC8xq`utxak_<e`Wy&MfHkFxdc~@I`h%U8e~}9@bYc>7P$Q0S3SwJZzX6bKZ*Qa~gIEOYXRd1T36PM9
MZXi%J_K#s82hXSoP(8lskx$blvKtuNt*`Nqp8bPGNRMvg9Ln!y=pGp=Vah_10eM+5H)c20`>FVg25b`OR-
E+UGit3`TjJk!bZznHkh8nk4f3gB6A4ZmggTb@pY&Sm|E-
NUwnd<!QY~nE5dVoPH<CfyWpBd$8zcr$EYGk!Qjfio0Qj&KB*=29)lV(CAlziIJlo1(Tg_B{xl#5z`IV_uuM+GONx1lEF8ZHG7Xe
RA$F@~hup;KM6vQfFlG}VbJ*Pv%>qFVKW=7-zZC$PmMWhDhe0777fv!N`|uM&<|mj3w-
E^68x>tbZ%nZ8bAZ4Gh>MmY7bh8#+p=HW_y!3Ho#0F@58^_on|zX9s$ck<giXWrV_^;$lxXP*97EqX7v-
t<7d(LOV7@h0J{#qN$!hihP7n*04f5?iJ*?-;jJhh}L%QMMzM>8z$8rB{S@3Mle9S_hzzI{S1Z95-
o(*sbJ&J0(&X#Ws0SdX8=mO!a=^XrLaQEW{_+sx{UNCAwYEBP&elWoocEal%%f~Z5Wx#1Qo?yY2_bnhfq-
^By?NfeCusCAxOMcv<Ivx1ys-VPhdyOXoV^pG8hVayNc>I`Pe)uj(v2#Q)IEJ9D@}b0lsw=<)fERRfaIk0}ECfPlXAtPXBTQTOcu
StKyj-
60O<3K~JdAKkd&%T<=%$gN*mH^|$3j2NERHoEZaN44!FYCawJx!+vn7Q=DjoC_5HxSDoGSK%W9Q*nK`Axs<fQrK$%zvs0JW(`9ck
{cqe*joPT2VAv<wg(&tvkhdJ&32d`(RLJ50<)q_^MoA+xv%?wk!{?~RCV{8?RKfItU1Ip*NH3GMk=(N%*5sj@u!3;1R49EJMeInc
V#Gx)`y71-MmM3S}qRJ|-Z3A9-
6Zvu;T2JRu9feXyFMm2ge|A@=+uR(8sfcLjrs<Gl0O!$Gvehc<P7S6lf`FZ&~3Ebv)qW7YBepX!Br%@rt!dmc02h{8{I+dMkkAR3
CEHe0XI}9}^5$uxCqw;uL%Fi!Qel(CbZHcN^0C{%Xv(AH3nnk)B%5848xo$nc174^~h{^-
)=XAdNGlqxD7wzq5WhiopZ_Yv+17(}h1Nw+1R~A7ZpTRn1=kffG8q${UJTM$z&@7$<R-
xG_nU@*QSIJL`UL<r19CRq?10+ELCGdN0n?s}JoK}Rp1V^D!?3E0*K-
Uw3Ln2AgQ}#L2ZW^pZ$3t=?CdOl~WKz}C!(4d(gM8%JJIvZ#S;zCzq5Iq7mLI+k+DHqyR<ed>a!wX0jPv*Z^66JkW>le%9-
DcR6h<P^Ro&dw#}`erj<`Otyg53<f(TPb0W~2XBr-ISFU3@aH%`Ogxf&DKlt>wR)<%#IxD($_L9Z3)62V76RZ1CvuhgJ(mc_gN{P
<7ZS`mRk*_Aau8BMH5gU)Cf1{PLmE_7;rk_|soq@KFCDO!A<&3f(vIErVj)w<HTFr4s#=Lzs5598n<+xeV>9|e&>otsecQ$vxTT8
rn%10#j>ViDcJz%Tq_5`ChF`?3iE@MM-31KLkg^-bPiB2=Ps$CIegshfLd-gj8J#6Mm{%MKyH?hsSZc7iJLP-jA4<0cZwgR|KmbN
>hixkLSbl`f)dUWhh}uGJ_`feD`A0z)~c_{QWh?HS4Pt^xyzGtPgFk$k!0=Z$I7Ns`hLFN6`r2f839NH}Wfh!$PrXT_wvXk~diX=
<XfGc_$7MZt&8PlC<ozZ*v#)rxQ}xFcb63qRi-Z+p{|LR#-O+fGzFi{s0SZdI1T2*cul)h|HmyDW)kcuw5{kJ2TT#S*Eoz(qU5x-
5g6g*Fz+siF7744>p~dxBxD?UqoBxwOs=j6`ae(`zKvZzyYL)cKlOs88K_9969HWhA!lDp6d4Au!CpVr<Kk9qhVncAc+u{n8(<bB
3Hy%V5r2;-
%J!dpv2Viov)K+ZOs^0L}CEilUrDJ6&03Nvb(Q*kl`$0gVR@UeI*k%O}#0W~k_qPA%s04KM_4vr%$}4x9Wb>l%WF(c;ae9^q66x`
8#YHLkf7{La`y7-
=Z;H3I(PNL<C3sno}>;aq{$cv8%#sR^Lswqb(W^jWSfdg6hhK1tE!uoe?mCOJizKarZ)dW4QN*y|)CKXr|!480+2KgV&9mhM6zvG
9&XrfpHSLB<QdJOo?QCLLK2i)3b<DKE4S`yw;5kRFM);HUEG@@6bJxn^z0cuvgI9gYNsq*9(W8_EWSJy3_Yobe1ko0n^E1cNXLvT
KaxZPOpbY>XFv$$UY;%!ke)88yRhMZln`2*z8E=ixuTWqYxc-_?c!(d_z&2ij!xc4t+&B9z6+!rk0CKzNVeph_-
0%Qwxn@Xxg`=;U}a)oz6i!E!EIxd3N)56RnNf!kzl=ui;H{T^&*JJ*BFd_#`_iwYSTRitAbT_vIWi*RDJx2cGAPaZvlo}UmKfg$Z
QST)A!!QY)H?;Q3bi#;(Yd7j!Wl5wXa8U(?xXbinR(B*n3(JTv$LT;dLlv(NM(SjF(mkgAf(jFl1P~hw7GIheD6ZDSw)33BF2*Cb
jQE#ML=VL466UsuqtH4<|5qDGSP7UNGI{O1j`iJ5CzE6KEu^;SnfJFGL<Ln%4iswoA=FEU(PtMcX@^F*d__28WeuUxp$v2G=qWG{
0IA?8tE6=e~R@ZLG4erlok?x^R0VBsF7{eNkhwwEJc`u9JSIzJ+D82Rb$ytYmNd05nwEY6loC>G^2VKZ-cwq(A2s<iq`Vm&RNsf(
!%H=*&4@_^qacyXF+!?0>v+y{~s_DRm95>vyk|Z{B)9c1-
dSsjV8gA|x+2>yKBrm)qCB)V#sljb;<2zde5wN{mRIW3xwA9Y{shR}!09R-
W*sbpzt!mLv%x1wyfAOQkgW)!`OD&IjG<K|$aFytU7~N{?hM%LM0WU)jztz)fv*%C;wZG~l4c?Ad%NlWf7Ia&Kk0sg(03&?cpAQI
aH!pQ>U0F_^Kd)k@#v^ZtHNcX+T-
`3EM&4gKPjMg4ADRO#qm+iRwYkwGLZEIawYlWYyk?nmPc2@tY_rh}RfARIB{)c?LNCGFoA7plDMzQM@Nn#b>-
*8sd!O@L^%~^BVFpRJZzG6APbEpRY~V36BSQoJbZ6#f9J=Z}jj3W4#cTyQK&|mtE!%ZMie!^swQMcc0h++cXIZV6f%2urX}}p&#K
*^Vv<C3r3ib+bcIIR1)fuR-SHhv*BWV6sX52QJj-7P0l=i9L#EYUGJ)kIg*gJ0BoZvf(-
Gkb}FT6V3;14PDAuCRg>8Q*|kaBo?sIXRMibb|_f3`T}=GsYP14+sik8?qu<I9utNWM$<fml&dX8M3Dg$KC`+r|Cv%kp_ytJ?v%;
oj-d{{c`-0|XQR000O8001EXCaeZIJOBUyUH||9AOHXWPjF>!L1$%dbWCYtFHK=?VP|D>FJE72ZfSI1UoLQYODoFHRnSw&%q_?-
Dp3edEiTT?&*Mr%5%qV3iF0wq$0z3G#K$YxDnxTB0D(GGN?ixSg{uV$#Bu=uP)h>@6aWAK2mk;8Apmn-cIv$X007Pi0018V002*L
Wo|)dWo~p#X<{!=aAj^mXJu}5O=);(ZgVbhd3{w;Z`v>re$TJ4)CV?c5UTBALh3^bZp##!C=T1CX|mj4z-
kglwo|qLeg+bQ9Wx$6;_v(J&gZ-H4M6GQ_c&$+ttA~VH?&r4%cz)v)iMumK-4NeE;-rI4M-
YVM?1{`qSdsDf{MMfT7oSXU^QRgPqYB>Rupsw_DVH!7KS^f_U+50;8nOMOf;;X-
iCrUe0)%hwe&Sqg3_=etPWpVR&GM$D3qcIg00{cz<ArLR#1!qs~Rp8Aa%_ZQH<BJ<4jhhCOay62BK1G7!cXN+Pp~;^^{KWDFFIsm
V?iZz)QynBD74Nahkygn8D{cL|=|bNAJ|9HEed*p>lP|;uqs9E!!QdyT5xPY46PlPmqr;VXdFkiO&(DS5}stQyb4|Nq2%&E4pFC%
RoBgt@J|2N6dNS>?h|Nj;MIkHRhz*xIHrl5ozesTb?WujPfX7BOJxc2=%GP3-
}PN<J@AbqO?PQJuP#H(r6BG2G6m@Y)gxeqP&_hLpTO;aYm$|dtPp+kd8EswUehLUcl_=%Gzlv_#4wAYquBaubPr5dL<XVc#vOSE|
_eHD)vq+=bR*QpA)!Bek_sexwBD{kE;h^81{K+%a2*IPMza0!t69F4tjsx9FUCem{j7!+1i}fioUD=SC36{t#_znIHR)BokvgO?8
@2qr2goGB!$n>BYe(ryu8OhVRq<xa0f=y$@j^0e3)R9;{==CPQQH}fg7+TW%)vi*C4=Hzv|(22mT!0jJ(E1r|?I1y_!|Kw#>4pDG
YX{Ee!6NT^DxU!}XYTE32oNA=)oEpUzM+manwlP-eH%0C$>cXy0n5q5M3PhEg+?JTkYDd}_Ou21e|P9vZl;=^<)eE1qpTcfgP_=v
dDd1{Z}Vj`LM91ntYh6T@Zi`BP}k3{CkP`~y%+0|XQR000O8001EXCj~M8q7485A~pa38~^|SPjF>!L1$%dbWCYtFHme@V`XS>Y-
D9}b1ras%^K})8^`g#o?>x@kz+zpv?V(hA*xku1yLbIuH_VMCE{=*m(oSYJNoV@%V7xg4FdF6{}t#f^iR;o$qTfP(3$<-
y<O5yTA&IL^LA$EYiDO?X7^X*;?>JPY@cRhTGVv=WI~H3n`X2ckh7CFThpqXktCTenngvEgk-aMSv4drin2+YtSss+j?=uKXT^<#
9~JMn#LsbAH1wg#vuin0QS~b=Cgn_iHQ9`AZ6&Wxk6s*qb$<Ht_;vF7m<$2GH!f%MET?f5T`l9wbo;xb?LYOm_mk0QovT&U+1eWC
X<d`^IW3NEK!aCRd7n*abwR6p&}^_p;4g|IIleP1Cp1Udrr8a-
rTLszHOYzz1qx^a!jw9D@y!>cS`;W*52kN1I?2)L$<f8}1&Fp}1C021Q8(o*8jz@LZfO;DHK+ulNmVWy7#{FX@#P?GZ$i4M$~%NU
q?s6AahWD`O6EejxTg8EE0i1HT67hxX5SsMeMsu28Ys#V4m!bj%;)xQXcI>g6m_{&z`E1v<>foz)ae0sHjg`sP({I03QaGY8o%{;
O=w<IMNlhIl+`TFv+ro)s3SiIDBxNJ<j+kqBHf-`Os1=xskwEuWXxrJwgq6i$eV;AfPp93xVZ$LU6gRNQF88zZM(B^G&-
6)paP#;R*npplI4ht|C<^&>v%?++j625O6OT}N8iVWGHvOktsLRRTrM680RJc<*YK2rC3$)c*0fC1C2X)|!Jtqa-
C4Ql1>cAuh8q>$(Ahjs8|p>{ISxyer(=3s=8O^qCsKnm=46Ua*)$m7WUPQ8lGP<nn~;XqO>G1SGlac7zIgHa<kg##^RJzVk)lk=J
y3%<io03~O5~ui_0={6L>b1o1$<a+aZF6MSQ?Kz*8r_mRmf3zo5rYUT9*Z=oX{yK+aU65IYz{ofj_=Yn<Sf<G;xT)kb$+RK{gu;h
a9Y$)~J3`q%(@BN8={Dr+OiYKp+gkGjRt0f_ZCWvYaA7u!SM6TMF|ypTJo&10Hq4F@VDF7IXotoFf?t-
8>&>o~Cs}cF9{00ds0ombqs42EJ-
E%LF6lSeU7z^&E~{OWpK7&A<h6n%ESM<T%0cwx~2u=Rh7&kNHn94{Yy=B~@0;7Y$IpgUmoF!v={MG>@-
E<H6>m9`pv%hup<xgFfWjthfWOW5yA`;h=zBM=-
Up=}t;S`;zZiQ0&e5%X6@NZLbweJeW(fUqrINID?$5Ek&o<1M^r|It&V8#AKUsN0mO!z76;U!h{KD-_`-
{50^afBvQJBDIF`i_V|FQiE(p8z9(Oo1=SLKs(((h8p7QBB+q79Gk^tcGz<b^^FBeN@`$Ve*NZ%-
=3qN0^930a6d=YAbs(@{i6iLGu`M*79hVT|Ax~({8!6fVwZtZeq^~)f+}XdE+qROL5M~|ziI)~P808QfSsXmtOpbwoPAq;oXQIU8
z5{sEXvr~GBtnj28c&NN_o$1mim3N(nH4e2<1|)F6mS(;)@3rUJ%PFFC&oz^SLwTi4+oL}5HG8<0_YWEYM`_8x#O5fK{0h#A3a!)
461+v{MSfh{K(uX3@j!xn=Bm+KWqoX5j258MmUv)J914c<Qw0X8B<R4VqR%6=c^-
QP_NgE)+RgJ#&{mraU&89BNL>2!?qJHNNSu?s5gZI1=0~kM)=tJ<;HrZvN?CjeVQ+*m1x1bdlRi1vP!VI%~HY9?x2|<h}P$ndl^i
Cg?4w3pvHgnD#|PrN6UzOhIHWn(JEqI6*EGeR>sSxuG5&_V_GHBk(hlkw-zyxDG5POd|FP<kipd*h`}BKYFzLDg&+lm)28Cwx;h!
^3YK6d7bRh(4@&{-a#4+G;!IL(-et|LQAYRb#T+6)UB|}{V>-
toyk%!5D<~NYn#_}>xS$_~H)O&c+EU6?)IEnxhsH#hRYSq_T*oX+ItXCPB`o%8wIbVO$<}!l*(fcy;<Z{Rua@qni0I@$Y4rrovWK
i_bp((D9iuT>-
jBB4QBE(Cex2c?O;mxJ)V!Y1)>z+%z&|m?a2;M)MlGs|jJqwr5XY1enZ=ZDPyokKv=pHUhE4edT!x^CSjF<8b~xk1+IrHsYpmz3*
VbFlrTWXP=LoRbdd>u|^@1XPjP<PMNVsbEE?3;?S<`#Gu<vs8SFg{1e*zoq!f1UYKesEhNe&NPPv<2uTQ3$z5yZiADztCv3Slg^<
q36$Jo0KmY@@wA{_^OX(>KZ4`OD+e3vc@<k?oeBw_@gO!Mo#&MZB-
_%e=xMVp_>@kmU5}3sBaSLe{8B1F0U3jr|HMXXN0l<Q$M`UZ#z=M$zRgD^Oth`UY@A)g!ziRHs;0;OUXtllDnfH`WH>oiC;1Elov
NH0s#<9CM_D>%1J_y<LEahX*OSg_M1G6*V`5ogF$Wzs-J~O@`0<kNb~5-
{0SVyuY`%+ke`BvVRpF{`A*>{_Dpd4tCN*asU#P#m%9LF9$nfWI#ehpYA?+`uy`Jp9AgPC(m}D?(H$6Km3DHBnNbMxD+d}I)G`1^
;PlHpZ`t{7Kcl@)~lT*^K?L1z#IgVgE5R8F5R{epfJEy@jdw&|6LV9J@)#~_xJan?>+B7-
+T6C@9E<`(Bt2K`^%4(X|h7ugzIK@Ex3YRg<LKg2is~}aC8vs;QEmDA`W)0L9v7EaB21{04-
x!f)eYoETFD*Xlp0tgn^p&2_UP#2z{7C)`1<HL&i;bIOAkZGnxv<RvL<bZJ_2q)IS{*Yby=yPmOBsaeqsK$L0^*nH%<GD>LZyHuO
Q-s@Q5;-GCwH#jS0vrdznMyLVak-tRbuR~>+%H%cgS8d3Mk88&Y;)qd2D!;UuxHn8GI$Obm7>dO09k!>@vYH+NGvTzF3<#jr~<7e
xT$-
8c;UcEj(JNf1;IX*l8?Fqj^VQIUhW1Ub&?ZAt~(E0Fb=&10;ciYhiMrGGV`<QbB|FC8ss1iMRy4bfBrlsD3me_+FvT`2D;iAMHR*
tbxe=Vkabzr%7Y0=a%cDi+vbqyMOYd+0WRI$hq=d#X-
1lkNB0BZ80=F*Lzb}5{hGC4Uh{_)klMCeG|Yw==Uvu*bun1zRAxzg1&uXtJK#JV`aKV4zl!}5N?8MZDI0x)%F;J^d-
0voUlxS>+>;PzY`omEG{s>y{`?(i6^25~C6Fzj6Ud_fKNV5dM$%WK})G`6Rq2ZH-bRbxvF0uX(cD?1zFb0w8_D-lM!%qShc0}ON6
CILhq@#Naue6*1iqVxtwAlq!3tT7%L&WiiPxvcBDw$K188&q3GU*9>_6`MuF*_N?0be@i{qsp%PHc)0bZR%dS{5CK^kOMU(UKIJr
wC)fC6kB+jxC=5{=?lXby2?@bv1encu%Ns|V0nbLVg)-z9e@fHt$u)>$PQ00RL(|>zK!DV(X|8YM>hoJ-<WL=voGjHOWBR7-
Px3TUciJle7m#lGY(Oc7q4wv0#X}P6l-
=wYC+n4O2=@Li??~}5r<tQ1d$j~$V2%xKmLH@bA$LIsqq`ZkW`XEvYuA)aEQwkBr@8h80a-
iA7UvSOYeqxI=h~vOp}2tz+#TKk&`6F;0<}Md`mL4`(=(6hP}g%>WC(H22W$zP>&5cTQ)S^*gEW5hZc&A0`coan-
&WJb_!sLv<6!z1uZGO!6T3?m|>)qDY)mY0|#v}Q;l8sYiAs47qQnm#%TtNibi1p#ytGkuDTqx)eq%71a0mDeb)8}r>_HQ;d~uyd%
06Cw|57lj(ZLp4;{Kj;*YACUv666_Z?5(=M#Y=%8NU)JQ0s8IHV{KS`4kCH?VZodr0}66G=Y7=;D2dEOUB~rz>_DEC$+oMEzbr^6
6qd)(Gfe;f&NqM7i^{7La6t-pw;2YXSxbA7}gJM}W1B^dY?M86oD@JCXoz3+F>vTN8qu<)f4kR|(g-
jK7OvfBKc2lwsun)@A{t))l`uJL8XFLOB_S8kt!8;eg}Q@?DH|Qugj>RnWXEU&tm3E9!|RMbGQe><vvwYlNX_>}4*j=M;a$(W9>h
kIn{<F1!TUqniLh2J;d8<MyN3_M?eSuvJ;vL<85CPPfE+MQ+G6jaZW=VRxlWHU=<yBkofc!PhGF+vIuc0d!2Orp8n<7K~imC`Js5
goilu^4Y+jgkaoKsD7oxDS}WMrYeuKr(P=Btrr}8u6Ym9cGbX*i244c-
RkFLM5iudhp78BWkcg~?Q5Hk?>e;gXhgJDKj!I3K$zfr6st36J)hvrKl~BJCJ{W3Gfd{7ldr1~5<~XltgI$<F=z|=ah(?PZHPbJ)
$~Ln;8WC`pgFlOLu!5}wf^~tu4wHvT@?3i8-
`nG11Wr<mo|{HI&iCBGO*UbY<?NrGIZHy_kZoTO8;MN;g5eJ#e<V>yR2!08>;=UZ*=evL%`74sjU#f)w6C9wB{RPAAfqrDabcxR?
L&asXhK*zpXV`@HrcAVU!}G3^v<&o_jFEVD*Qn5Wd`MJ+1<7Ns{JylBizAC(e_=Px!ig5_-
PVf;$gXBs}m+3c#bS{{T=+0|XQR000O8001EX850RroD2W}&Mp7|ApigXPjF>!L1$%dbWCYtFHmfCXK8LPP;7N)X>LMcb7d}YdBs
|7liRit{;pqvs$V1zk50c{MxD5>U3(nIZsPQ1JRS-np%Z%)p%COL8rT25`vMREN$D<*J=J*561Z3__T|~d5`Ppwz5VOIuD&mGRU3
8nvQTwfZcEi%i`OsT&9;r+i!9rAZP%zQ6XpJ(n^wrW)~#$yU7H!x6tb0hC5=(W5%oif0ESh;gzf3zNnWdVr;B$m)ITii8~5}{eM-
c;f4_Z}J$>=)>8qDN{B1TXxADmJOu&aG=ekj8Rc_K~iC3zrRW+Nvc=P5}_QRX($7etN{QWzz5_<C=mA8xKY?fuRs$g>~@t(NNpWJ
{JUTA&$RM)NgwVfwC9`kUcyotB6&3A6-
%|X?~<Zad6l(ie?U&#1JWxA^8`%ddBUhczeHv6tu;Eeu?;dI{nd=AT@DP$!Y1$L^%ovb<~wz?4qnj&^E$D}i&$N5I=<w?lOXtD3W
kV>>W1q!6)t!6|~Ht=6{O2yAciS;^{b*`$_yQWj?wP-bQGp#=G<gRI8!$KcaL!Oa<mlQCqAz4>xn$j$g@leT}SL}>xuC_7<qZ2o#
eJpEpR88u($8z)X*J1<80#iK)=~Xc48r=oPV;fllX>@%JvNk~A_<eV1P}cTDzY4V#J83dzwlJ#NF2&WKX*Jd}b0YoX)08PiX#~W=
aM=m#4UF6y?==`;Q+e$lFo+7&lr>(98)ggk%8=+>v}O8<Bv~!@iZ;m<ZQH<h<T2Pcj&F2v8VniTHMz>vo#QF~D}K<m0t)=k+F7=p
xlBVsWtG0U7FB85_przZcuv8;00m3XR|eK@b#q!F#nQ2ET2*8c7;h^r+X>d~uB>mtOES>4G9mvlEvqfl#~M*=TGV@eMm3Fw*?*Bn
J^M9R6krp4_NtX==xd0UoFqz+=lN|T*>cJ~hM4nk{~)#B;~?Pc`$Ox!1AgC?1?tC*d@(0zVPCsFP&hMr&7i>^;t?F`S*vfA4ciG>
PNr4+Oy7Z}U?=CuwxHZyw%158LXN#M1{5_G6ixULL3_9S-
JCu%cFxDe1Lh)Vv<+bKXB&!vdH^S1E+&G^+K0mn$SM#GjKmNJo0E%!1Ja3|ssPnpvV%kkODKMZML`WS!DS$!=?45?9LshGNs3t@r
XzV~$rnpVS&&81r#2i&`1Qh^1^tC-gX9GeccX%MjImlbC2*3}1w7ixBJ*U{lQ9*u9rCukQ}KA8)~tZ%avI3!w1g?yEkX&T+;pvay
eBiHpiI=cA@-
mMux4Xg$DW|a@q{W3lOp9wD_j38$fG_I?IfBIZ8e%^z_UOq+DXbPO?VFK(|&bRm;F=)tHg}j<`fUGuBr>%ml3_9oFJY!9X+FTF=B
~W-
46!Zh)^g{2pi6N|DcHMBLH)fU=l3xdNLaa&h=j@g_Rl9CxCt(gpAoknM*}kp<oVF`uXXqDsOh+msp6o`3S$RdIpc+e9>*HG8Y@aG
zNk0V9~CssAjLpeU3W~OEIU%=C*_tRSn<OARzhx@VJ3tSq635H|d|!Z}^eyV6h?26w2gHNtt<wK(a2k;Fc2z^zjq#M>YG>;Bo+(Z
Fi^?Q$dxAREwpp5`O8R2)4=WEExf5qiz5e!LRP2+si{Jmc?o-7Eu&BHzCOwmP2X-
K(&`=Cb;ZlCls>2QH_Qaj#FU{1eD7b@YRY5g~qnL$t+4oocUxBaKx%3J2WK(T?<<;!3$U78;?C%R@P;kWfW9NP?Zo6VV1s*<0Ip0
X2qoOvs*gKU5h!N>E<MLKgT|fr{q=1>_S2w9IVSA=aAoK#2^9Trr&=!cXS}e9${gF(}xC@!0SgAMb>n1<ld_+*ZaNWk_b0CDuNPW
32AT|(Er{kfM^MuxKoatz#=@UdEkJxBKRIloK6WEiP(#^^t;R9<khNdBlFuEaJ#z5xaN@Nb`hyR>3==)U*kiKAD=kc_=oZF#*g1q
-Ufu1Yg|uw)<7f5N^a0?W1+}!Fcc@^4$ApDune9309w5Y3Ba96k2?iW4W@-CGvK!OS@A&ziFCi}za<etZ-iC<Eha!itng1f9NJ+O
{uq!2R#=5UVzS5vtJohSLNdXM{`v=jr*hn9uu^{O!+3-N-dL`nT#1{YC`rV803`E-
oWWNQwlpdYWZD+bISWgf&~nSTi15n*_CyMr04<=h--bTmhW&mGB=4%oHf3$6Tls@RHF2$)y$gjzAiXU!+1V%X2X=^Lt}_yYd>|AO
g_8o6xatc#dCLcsj&{(QB9I#`lHt~}%$WiOqw}HH2AsRB2e@jU&i_^?^yE4`jU-qA4!Q#q84cJ%z72e2=qnVJPA(XL2_uI&%BIEw
%X4A2KyDvR`B)CM9<~h@mS&(uI~oT)ezx;rJ!#KXRxx5L%SwR{%qOOPBvM;D|DpMm+5v=*PuJojDD6``FAPC_tTWtSM(xWff9#V1
>6+^-
^gS+g{0>LuJz*4R@J=?yI#+N!;94HL&=X~RP?;ya1)P7z2LlXk7(l$H1urn7=kJmF!_bMzvy)Ln(W!~ul%zP5LPM4HgA;j_)I1;y
(l6(VxN8!muF=^XKahTC1d`OrA0R1ZVHv&OKs4<1k=wxRPi1S*EBINjdDRuI28VAbv|6Y*4HQ@s(E$-
b8$9%LZH|F~HH}}(_NCdd0H}TUni<>fH7Cxx#kU>UIj>GwiXk^CT7_pH+3*h1aC1=&LRk?@OE3j}h5BkfU#9T8JS;|t-
%lC1g)Bk7f1oYM`xbMKH@_qHDdSEf#e8|*(T5J&FFJDfOGj5LvGssapp(eaXx}uL>|MA|c(5OxfX9dQkUR;O;M_NWiwiqug|0%E9
aK9scV$^bkEjOfc_x#)UiDI*m46j&Ca6H%H*?N#3CHO&3idRrSC*+f;DO#YpC*(45J0$c_)QREi;W2+8Py3>crq#-
qB{8^ru=AM8A&Sx0gCKey_ap7Q}lW`!Om1yS6UVUusny@<h})O%_P*D0gk{K@Os<TIU+$yl&%g5h>@!2=BQylEV-ew93TyWh-
bvYeJf-Ip;Vl%n3Ol+i!@|HOIDCsg)~>CnMNIcueS>I9ij|-#<;R`J{6Tk_<T?lIQIUnY+OkV6K8n92-
1>UF7TJ$iHB*7y55(4@&D&`PjwAPj#8l~92<<WhF_{8CFct3kKl6aHTU;$N9*<3gIE-Oe#SssBTKEwTwZ-
B&X<j0yTPxb$bSNFJl9e}M#WjR*+#ludf~zT5y%cv_vq2>5x-
GCJtz_!AtZ9hix_qe7YqUbErYKH)VA;a!>Vy?5A?)rz!doQ8s<8C1Ah+MD5BlF?MM(G&m8SMF@Ynm<HoI3<PgkVOl>w$UjIGFfWt
H&m^DZg9tirRc^(|Bh!z-
T5w7@2F<|t8tcry_gcfwzvh_Oc%zd}p^WDFwNj8X;`(5Hf;Sh@TRYe$d1Bx^w6VO$X?c6EkV_==&_~YjkI;Sbls=X=Z_SxuwcNS4
5vDdC-ktDF@5Kw*}9Dhv&IS0iI9#eRlrs?tm4xgJADK3hMAq2<o{myj?F28U?9oW~F{94nVl=K}{GJGd$=ia9XD)*u-jSc`-
s>1bx-0R83=m6laH2`X2J7c21bgnOQ=$jzR!Riyu8Q-0nC|yIGVNH~MyK1r(ma=-
z)Vgl_XUwF`1KxrnJUf~Bt&VE=MKirkv$lYL-@knRhF>E`Hqp1?tJ#NZ;J7O*bz$$my_X(zc)*-=gnrtD2Rzsd`t8IPb)VnvB-Tv
&mJQU^whpW+Dr+NC*^4aZROe(#U1wO;dke<RHbe<qL2ujsZ6+U_oe?8D(aYKK8hm!Re-
&yW_(i(fFY~x44L08#kv67;pV8{>4q1HPU?>llFw~{D5M!?aT@UY*k*vcTf);0|#J9x}Hfn~i8_*F{-
a#1@R9&z6p5S_I1xWiB1M77X4EL`C`09jzfbRm<YmZ#m0y;LOy?aP2V`b#78NkfpZWh4}#PAeA_Y3C$`12)SF*LX3!R~=P8$i`wc
!H9h>8DF9>z=+l>@7h~^)(E^-YQuGrpt4s3iGYKm-
*P;mh^gL`KMFcl;GgfWU8>E{Z(YAwh&4#Pthe$@G~f!v8W~yoB<vvzKsC?f;EtScxUc2V}LKmg*VseNS<TOfj1MeQK<VXbN#Kc&)
GqLQS3`^#bVx2Ms84aWrgR+ez#16{Y1c@2k(O;;A<L!yoE0x(Zw<bZ+p?pHdyec%2|p32T)4`1QY-
O00;m803iU+iK3Y@YybdM`2heV0000_aAj^mXJu}5Ole{-
P;7N)X>Ko2Y;|X8ZgWL$XK8L_E^vA6y<L+VN0K1;u3wRpJ!1t>C{&RWB{f>0j-
se;Zc`GCq~;4%4P^m|suY1tbY_CZ>SCGAzTMmG+1<m~z3kb&oZZu%*_qw#^ZkO^zc7Db_a|Jqdwh6&C4eHS>9Jdw!~!xSJUk*iJl
s9pJ${wEc=pZT9zHE*dD-NLPv&{q7K<XUN6B|jUVgNwt5q_cE;j9^&ZpC)SgotNO|r7A+N>?AviXS0v{&n*JXh}@mRIz6owXOs;!
Hh%CVqaTU^K1z+FUj2>#Qo<{7ozBm~vO;tf<t_pPQ;w-{}vO#l|-EQhXn-
v%1Mui+|iyZLZ4K`rAdjT52d7_F2~CpM9!+wfSnjD3-
cTTdef=d9he999QC%7=c`OW3wsd8h+WV^I59~DqrU9MO6;l<#4enXE=z%O_SG+!uhv(`|W1A{82o6p8s)^i-
GE>I=c|FkuP=a$Md3nc2TvJs;kDas4m)eEzy`&bv}gALbP?=*JApe0?R6!=k;(^%{R+@D&}WV=y~pal!(tGeD>Gba+446!Pix_%(
Ieyyl87d8T9>I0j#C3Pm4x=dm?81Jg)~I^(Ah@;mc}Xy~yj=f+|&0)4%!Mlb4TQJbU=)@$~s)Rq(}CBc|!ua&s<5Srw&+F9i|<_W
gN&E}E>b1_=x-RZ-
6*IC}VXX2|E^xfqb&Rn@CUM3;l)hjm`!Qz|@2=r5Fco;RDNnCFjX%dBaVsZ;dDt75tQu6R?FBkXsYrn*G3#v)>2&65Vo2?}dw)$6
>zIubo=Gx6jiU#<m}3`M<<5WqZNB-
1)?s^#l^inW^Qyr_FkzFhQ^!w0zBs4e)wT1>|H5Q_|_msS0$S!c5xtM&WIQIb{yr3_G#5L2uEaP<m`iX|pWG~<`GnDQilBL;C=y~
3Y;UB1o*(<reT!*`jVXS1sv(3REqM%OfDm)FgR2{)}k8F(!Q<~$cHt)+s)S9vWK)gVd#=7;CMpMLY?c{)hGuS(XvVxcP=aNalzc&
b#tKg{2(#SFt@@Aa)Z0vHZ24rSBpBO&0Ef(EH?x4{Mont+ntz{3kbVmP~;i_r?u3=v)DEC^!zrl<w`s_Ls`QPqj0#(XYGwn?foX)
kioYPL*P+3cbybEMJR(w&6+z6nn(sO(JOt$Pi;eGBmsx}o7hoL!JZ*qk^80`K%1W|Ww>6ERDtrrm`cENVE6vPFVoAErv0bZkP=9c
fuT!SU=;^Q_H8tAIZ8`=&=Q#hlKk!1sE2IjiP^kB`$$yEyzJ?c4NQXP2TrfEkKq)YBs)Rt-Gt1FA)Xv{TOV9y}9oidoxF#MYH#A$
LJQ*H|6V#2{IUK6WextC#G>HH~MJEz~Sd%WReR3b8lziLAvpLEG37(Kf6dd?a3_X@4kw7wcaCMgz~^%<{F^F!7JrhlQ8|&urAN)n
#=)yv*uS3|?<xIQ}SEWCbjvwn|{g6E$RNU5%1!0q`abc8Gdv2(8Ip=N*IwoNKgo`mfEjjgm%efBC$}nWEr^UK?V95tlw28{PF70S
_;0F}Orn-drLP&Nr)dBgsSvrXYM~&8#TK-
)4eb24bc_P#xdv!)u!|Er9(GGhr~?9TR5e<!n<dTS0C6a@xy6uz|BpIp>VFxhU3a@f%-
iyewYJH_a)I_H^1GN(Lqdp7<y5E?qx`Uz+C{)WybQV{aJdfLP85+rh4!2?48vz!W!8Xw>;qXb*y9+e&T;p@CwE2NwZw{pkD#*&tF
6>!a*gGs{Y7k*yeDG!y6^W6n@w#NLP{GdVS^Td)cNXI==Z&4HD4^=#0!wKxn;up<rE77)y1B_-
I8iG`MgxVO;Y=`a%%RnB|5inohGDb8q6p1v(Ti;*}K_y}%v2*i{SG_j&8A@JtSOfXqdytySwTgreWWz-
(oW^Cgh<B+0#QVsH2uR?}vlc2s}D<AVKv85C<Asby;_-
B_{p|#jyv&{2#@3><xmRl9!39ShtAuUDFo3GCFtnxM;b;E76oDpga<$&H65T^9&Y>D*K`#>BQw@5w(;qCDk9lUF^<<Wa=aFwm6Ga
&}&q6AP?sEk6Yqach)Q7)>UBx^}{wIs`YK1%)ycHd=QdYd%IQxv(r=_~QyT@G5B-
(f|(5KKa^hL6Qm3N%U~^GnrrE*E=|H^_w)rU~e-
N<h}|9^18r79n)qx|rv>1<`zie52a5iKGr|VFANsQwEHVhS=lk4nu{CBxpkwl5-
fK;rX&U>!o*w>#Nk|#qbgQnD#ReA%$d^)olZK_R?wEPZVr?n~cX|I>aa!?Q{z8d}#0iqgPR~&5SigU5aeR*b*`Qh=fbHG$`ll0dm
E%Fjkrj=lR(N7AA2zuuq^E(o<miVlA3>+$FiSlO6|DAL5*9qa<q5-4_g)kAVkZC+_2Q)o>x%S>!v!hIB7sU~iH`j{({E;`)-
<lGSYb8cbvjW09)tLTqOj(<MkmvS=gt!Yb?e%eD(}*KUR#0s9dQ<2;deyleq0RIR~mK3CfqH|p8@u{T|U`zW(u%!mR-ECZrvO@WW
p`3$_6qGz*aA&bvN%QX6?GNAx-
<+VapVAWh?jX{^{33QRTKs!wX%byh;>ViE4`GNMnT23BOq#SCR@{rEaK~8Z3dHiNw2|b+JI242+n&u<`czpNh$FEiMKR&UD0_8hn
yB{{2^;#g&^z;ZgBiV?ZB9~}I$%YD9gd?lO=m*3v;7L6WKQxK#wIP%NpIo1%IK;PipCx@;G^hJY(`EIwiIN}H8iwlFa>*_=Cc6Kp
N+P5;0p1g1!eOn@qp~ORC?XMiVFDFJ9ihr6cO<t(!}-
974u!4VO1x=jO%}e*a4I=8=>){6r+jakUc<@E5dQg8=nfb8o5|>l(;L$S9MuTe`ebRiX^Z6$o|@hY(P@T<Up<D9?7e54Lx4gkP~Y
Wwild%pg;;zvI*;qRss$@}gokXj0Z|wDUL#ue(Uj;QqR>_k{$ab#RU?Zu6NWj=y7<|lkr=dv{wYR+Dnsw%9M1t^njWsJwLNhDO2+
Xp_FuWzq0ntf${@+XS|XAlAr#TFTZbZy$%q02Q_bTc%;pG%25`2SlaQq=4TaJyg+3zP)D#c^aJHS}AAc!Z{eqfaiL*M-
Ubz%ys)dLM*|nmf?<;$0i2)PRH4GFNWf)n>J!Z@rp-saRSu9Q<#b>t^6IGiDo>Slh+LQ%FUBWpCkRKxBt(@(WuXFHX<X)rNx&kpr
!8?Ls0QL};!{vr>f|u1wwFuCfsT(%mn$lH?>KdcrwLE=H<*U%~l->+w8E3dw+0|J-
MX?D=3E;Ave>SD87jPz73w^98#p<`K2evAb$eePPpkfmdZ6fqz<Sw5rRvJ|cL|7>)h&Hm#vK9LYD#8P?@q%XQn3oi_h%xoX7T$@0
O-
Zd|=KzX!U6O?g_BcrJlIo^YT!umyoFYAlFLl0NW`flyJ~HTRhf%M93V$pVEW!=aYfP!TCZ#4@!jaDvGcyc~qOVl+M(OB`ar`QIk+
+E)a$81KgQH+Kd22E7SNYX|iURK5BsjB4_KYDM&UlKwXh;B4R!=Udi^pDRJsh%()S@P$tQLeqdREUMyq6|t7nQR!Q9CgG-
o>B<gI$!$;AW|CXq-;KBjh}9-qrA=X@lFGB%QpzmX!D!G|H;9HIUGt(c%_EH-
fb$$8VHWXFum~3MdvgQ#Y8+U0Q`fhXRq$^Oz9SB-
qipz)Zkqf}FjPV`~FErf{f0j$;J^g7jPINm?5_bDS@OK#S5nlH@R@cgvnI7vLz<0Tmr-_JkQYJLMq3Atw&8$>TN2!$;QzR!Ym6n5
K86z$Tilr2(JoG5bC+jg9p;PHy>PA!vw>lNgN~ZMWU5m-z(AZa5sW6CGRyb4ULKWh}5*LOU!QWCAsyw!(+-
RK(hO$OhlK7TlLV{P1-8{PAy}ym<Ni??l7kBOwNpTcxq~aI;3EJFRfAeJGA0_738Cks3SLjG;wfwViN$U#gzP-
}*zu2<!ALQqX339I>9X!(zd{%PhmZOFeMuOFuUxvMIyD25#8EkYeJ+N^E*UUzN<}><Vkd1PJ`PMN-fbwlz$s6os@QUy$BX^cUVTw
A8G$9(xQ8EZ7E7=aYTelqhNj6$gI{GV^CPq0p9dQB|*|>$<4wqP^NdpcK5j<Jel#lPKiNhE_{r!5rgyIrbFd-
b<l9qCPfYx>=Y(9P{IMpjB$bJ(<B1Xs0)fsey0A8{}$Gu$PycRbB_zyz${+%Uv0%*&>t>hp<L%hYi6S#>;GVHqX$5W|Z^}EsC}01
By)Up7sY=cyfGdn(#J>i6kqK5T}U1KvP<&FgmsU732=Y8<%}uf#d94i5o%{0KDwQZ@VynEAW(RvF*Wg{?u^X#VC8BO%4bN#(WB%y
VI%KO<>uuwpf2=RbJ0>YanZMFqK{M1t`}OHF@i-MzL6>oZST0sYKab-
o7B=wi701EbNYlTeU}BQu2mpaNLx90Ggh~CkFbLJ)P#cw9e{z#}~Ve6>$GesYni62f|adELO`L&NlI&6T1dJkV3fwFLMAm{78d>R
?wWkso`w27Uin*b9n+$G}SVL6Pc!hBTsGRC+i;?fB>|yI$sDG)$p=J3=ue{4>{ucJK!U!W)$mk$fjl%nl!?A%*eGRxGQD7ZGlMYf
=+5X1wlbhq>VqJHLX^Y1|HDtg2#=)qee1N&?tc^6oL07>G&2KSQ6yXKP(z;*64940dxWlaq|d0v})~qfax701snG@rwc`v<V!I8t
A<<(g4JWTk*Hy#ABJP-
A^2K!(0}32L2z>Qz!L4m`KL8iE<s8tK@J&hTGtz1WQ|&IA<9u_KQk3hkW%5$Ne_G)IqY8ffod?+jc8+8*$8QL_r_#-
ut~8#+CxMRydeJC82KnMZiLdiNAjkL8SFPpA5AUcTXp4A2H$pe$HP8J2<xmBl4#Q{8xFWBIHn&+z#*foZj%}dsg4%oljVaOX_t74
wcgp~${S^$S71kUj}6m^a11tj{!4F-TaL_OHDO=VaHVQSOy=~`n-
^HUvyJHF%2el8bb3ffJ=PILXqVFEttMSfP#st7&tP3@@{kXyVUg9a_Q^ivavP^bXK&N}_0JM+v3W*4gqBschMiO%Pk;eL$U{KXQ+
U<$d5~No&q-=RT`UZG@6-
L*Xbfk|s>uVWz~|j2#e%X`0)UUdvL&4>r!M7imnCu_af~|z1Nd|<cld<SmNezPa})qYNd7A4pD2wW#BNbbeHKLt?z?d~`%jlo%US
aZRC6(^!<mroAr3-
3>RDa&$BW)z(I#N8w74ae3cAR^#}BRH)i9nTLfQ@zez=W2P64DuE&j8!o5O5A@4>ggC`t{vY&L=w%1TnYn~P2(fRW}4FU7CP!}98
M3k_MVtK(Y@FWl8my3=)~P!t(1$&?hjk5Kp#J8TDg(xYt7@}lM76J7W-)!3Fb4xg>-
96p_0+|3=+>fBbI*4e$SqRQU=lfCI0fZ(DBa-JeVfJAYY&BU4yQm{RM{?QA3ZohBrE+XD~Te^*ax$AV@Ua|z?K-tl&8g1K>ed-em
Bk4O5X2?49EjX@SUKBzuRth!x7c^q;JTG47C55$k=LNbo!3%rlhdefr#|7&6z!4T3b6jGb9%!4bWyP_gk?I_dYK^D6!{XJk0k{wP
)FyVCSNWBP-N-TW@y5fa`Whv%X{jdd6MYMq?Z_xLE;C+5sd0{~iMq904+}e{3J(iLkVa>XH>)B{qeG$EqVv9>-
ARDhV|*0AJ;vv}t~P6JLP2Qw$Pnt*lPrk;#X6RPvh9#a#cbPN5ZokfuVi*y8DGUF;Ky6Qw_AlO@@Ln>Q>!AZT_}Jf6c|rsM~0%d-
Mw{ES;(MiXILO(2Tj?$nz7>|@K2}1Z}SbJ&Us{`s4$8bw0(-%n&=n@PR`EJNOp-BvJ>1PV(dnVtGA&n9&!j6TCm3Ss1D>XmdPFm-
7%jcM_Tq~V@D&Q*iCTIFkV0nf=vvBHjakF0pQU@moxrJWmT`TW$`C7^HXfc-*ZhP{=Nw{{KwK?Zj3m|9|6i#uLiX4a9-
4)+wW6ly8w%#va6&4OL0?e>RCQcX|7UtQ#X`IA*y0*c%la}1{hi%I42t<cLvH!4f%u^NO13S(}LjHKk>+Fwa#X30!cd#7ugI{Vt~
%iNmin_5UYNKGit=YXL8f77HtmfSiry_io>S8TEZ#N45x06Bq3z641?zYFmr!lL38A2Q!K6!i3<qWuxhTdSK{BFei~L8VfNEclt_
fo#6>3*PvcR1R#&fbA<8vXvaa)mm|l(3k?8meQhPvO!36{%Eg+Z=WLJm>ffKJqQ8z}JF01k|U#;7#MCeY-tfs*apG^gi7BMA+<JF
6Z)%kpiSd5c^I9YE3qGFntp{HzUW3NNcVH|?bi&oHZ;04+5LJc7GMTr_dQh=fZN8bJ5p@J;=+V-5|ADl#;RYa{1njBz2Al&J7F-
{{9d>~)IX=+sSQ9GC@<aI}hKh&raSOd1cAgWNi8^KQGVu&dQLU6lDvj^T3(!Yz0B(4Zem;-
Mc{#+HMPp3Erd@y?3y6F#HKPU)xx#~&0>;ziFW^>j{0a?#o&y#xC=q1RTXtWH+ZICZb(cL8GoPbU%cCwqD+!0uYg<UxYoK{PZcA_
@&U}HlRgao@+6i}THoAt5~8+SSxoRp`j=K&mnx|M8PY&&L>6_w!mB+)6q9%nl{MU&^{NGBZfjCY*OR4YL$+G||`V;W;k&kat_Cqj
jd#q!(E1Hm%Vm@e~GgpcN-CRz=FpSk4g9Slliz$z<?MXo7VoiQ=eHPSFWWF!n?oB|L!#8K~JCxCW-BMmA@*4x^0`r|dp>S_^GJ@Z
6wADN)QEw`SY4waDp;P5ru2oVJjkNKACdmwK@$6shZ2zrb#O3^(63L;4IO%JNVu{G$@1F;ZL&=2{35CrA)Z?8bBhwHpv6%BL_)P}
Uq|F|jYd<E&q{!MjCE(cX8upk81T!6M$1oz?JO_pYKXPpb^h3EQ!TFKWmt5L<3z%u9<UM9@QzX4xSHlgvgAK13utv`IPw7TRFn7_
QO*WjNS=o6>PKZ{OT%Oub%=e^r43Z99ob3U;dnZjBx*Eh6YAh{AaLqkaCC@Ic``kYTt#jA@(C@&D=w9MA0HshtPZqr?S`5{cmj@+
=TRAWcNI50gPU}Srn`+@-
Hyz?HSsv|?*I+T<(BtD4>9I|Vy@jw79Ku}vcE7|wC=@e$HONB|H07cJv+|@wXg2Mu#jIT`vH=7A~Q_Dax6JyG#pCJTA1IRE4Td+y
NyQ*4@k~I04sTB->1ASdrf=jdo;>IvB&r=T_Mti1MkO1K$mn-<iTx;`pK)>T_AKYvvr$|qe(;E-
uqR5x?ZaTtZkXQ$bs%U%sE)z(go~)1$+wrXC6g4^YZI=OpjF+*8j$;!YydVk=L32RebR9)_8*A_@^5#5l5iSzs5Bw831`eKP?$Qm
8Mi}-
gt6$|PgxpD04o^cdeL4}5<cqRw1p8%nmM<~b@Y+<rxhC*8QED)=8t)*1{up47u1$q)Kw(670t!iqOqB>&T5yWVVC|qeMJ~)B44Y4
>C5(LPH;PZuQ=b9Sz7b$8w96)M6#y(~SHG24mW0d_i^^R#lvxyFT+r0!Bo)4$a<4k2nRm<t#08xQQ`MHAZIUt%ra&nQP5-
h5QA$cupyScQh_>rlYXTZ;2g_5rcUjV0IA<6+E!c-
k;l*!Sayd}wjm5sWO+v~eHkydkgg^o^@Ws*q=`do7+C`hyaQdi}LJLqY6)#aY#J|q52EN@WIX6;7P<*!Pcwdz3O}pi_$&eH&we9^
`HHSkx`Wt-9ng|!7sh4^(eT|gqEK+S++21Wi7(&sK`I~IDUgB1&zItT@fupy!{KDS*r-FtoWZq~cjDX(G=tL^-
MEl+5Zq5W8!ZxjiT?68_Z=!F5(5W=ZxeJ?)CozdldDZi~Wf?=1P{Jfjqs+~{w23?PGH4p~dn8vYQm)q%$#Jku+|cKok?(8rvs0%=
)MP2TnKNd?;GCm&3E$>|{vm5vBoCZ<L&ubJOou2ugG2{1Y}s>vh{Y~5^ss)I;P9v#-
=9jC2f!(6Czrk3x|Q<%kTSrA@M3_aZ8|QC1Mx{05GZTrjCKz542_$Std?vXHM|{%ar;pE!|9#;(2&NYYK~qYpZ$A9&2kY59n8zM!
V&_64UBgnr^al#nG4ZuS!4~QIXoi=8kET*CM*QG<&4AfkMfLB0XHm4yI>E&t=CR`L@B2N99>`mTkLekBF+IUe;2z~+Rx6;>hOy)h
G-
|fG;XvEkw>Sh2eeIiwsyLC!tJz%7IMZ?<LcZk5#bcx2#dne(R=3++&+q(BN@mF65svQUgakEP+A4g$ibHJc9$bNINNs2GtZ?9lpU
N6pF8HO%^K{8WfuNT4o2n>!n`86NxuOfxs-*0cPKlKq9ZU3l8BUM#27~1XGvNa$-e=Y5ThA%6q33@M+wpnwiQsaa!0xCB~a`i$-
j~Jtf5#jC9IFk*J!CNg`}>qOCg3>xU9`8l;57iL3}4?NhWcjtJ~p0eWHo7ajj43P+hrX`wE58JjM=jqA;U@3=F(DBUkE;4QO{o!<
YD-
(+^!aD#FCU#!ggF!c^QPJe8#Gk3x0^@q^#<<Ke}~K|jA0%SS*%A*0A6N@>;@B#RVXmWiv)A?eVy<Zw4B#dVV_CK)lmuRzX1{((tp
ldHT<yIN6Jic(NuXF+8M0PS$oSn2+x8iv9$Ob8Bu`*tQaq4P>eQfA7SN4c|e$vVWZsRn-KELrh+e?Ba{WwBIed}I+hJGi3Tak=&;
s*lFqFkPMeEZj}^5DEKAFjABKZ)zoU^h!>ZbA^|lFo2hF#L(V3UpYDqIcV$vOL}tnX+iOMR7sZrWo<y3zJ^BIvirp`vCMleIt<h{
oV2x%{kE#iAs?2Qz{Wc1a@TS&u)`p$U}$G^x+;tEo3y>YCz28$0asmBHPR8AZK%R1D+>)N^<=q-
Nn|feNHlstjUoB;hxHFB%G=H_c18ZnIhZtWV$MihMTjDyR0tOjr?U0aH&&=uF;ujqE&H{j7;a+|k|lK*mP3Uj<HH#aLGneFUA4qe
P?kJe1IfVN;dCix&fh1n#M88_kz-~9Ib!zOP`lz-
51<=c;kqaCiGsvGeBNR~I=H4tO0Y?`tAaUtu{T0?B*PnzRkrmy7Xl|u2O0kiPIVzFh?+iHqa><YzkSa%^0eU*N>0-
|>Qy!p*LUuit`3qrcjPNaQeW=ZHD6VOkCF{_@<9wG!W+M?x9m>`Fx&?n(g2&2n@BLS(iYjgqY+YxZB4F|gcWd#VFW*nZCoxBxC@|
YuZD~|LqRs!m{jE4#+2w+;Z~b1p-XVqOSiqEi8KuG&Yf%Y4<t_GGalBE<SmZ-<F)Q6;&5~0w-
cCj19lH8+F1#J&j$^_QVYR*K~p%E^yR%)5n3w3$}6A(sidg6Um%svC(9%R+n8e;WVF0+%fLbmV6-
+(C#2D_<q}udfoW>LaMIugwQ);fv#uiuZlGK=(^&eHX4}JcLHWqn=R=CV4P###o0)sp?Up1e#sn}hN^qCHIWX2MU_1awk2o@xn*b
wFWC^3I3X`Z1r%+~@Qy+V}70+|h+ebo)u(KgMs3&(>wsu3_adOctypv><_XAmS6MyiLi;m=su}#O*=b`fi#+r^z`KqigOU)_Sqnr
M=qnHIylv&-
u#XSi7Yxq95QR@e(D$cQ5mq}z<l<2!SS)~8<KmL#Zq`Pg!05PbNt%dIaVSZes{2kDXgHy;~Z=f95+O^oe5579+JI+&~c9muukX$S
j$TbU=m4%0_esJnEg@a%`QWIkZzvf_F&(t7><S66g7i&W@YzI+*0%$rWHrAXp+c+)xttfN6YJh&*u>D%7(I<S$5F;^BFi-smagcY
*HjJQ@!3TcX*w`@1-
DMk0C}m*6uP&I{V`UpyS<pb154wPBSC?(TWkCa6KIj52y=1n5#$pCA{_Fy)>~~uM>vJCkT0ZCkZj2>;yqy#6B^?bxJOA=O|1baLK
mDWf9&PA)6JVgW8A>_(os`nq4*~Ukw#x)_%kUBttnf&DmAxT5(g+fg2P7|xC!2gRJ0$()LuGE5a<7+?y%YOW2DdF>(qgp<vkTPnW
j<>mhYudnv#S@Rr;Fp?{l`sSs{;*gdEK&8z@|v@ACn8Lt6Y`fH}I2`D|;SfAa}0{qeFIO^`m{>L1N%)3>_B-
=}Mlhk2((iR`gBkKfzOe_ynazHQI_=dm3pqFt&VS8kOlQX|6&Oy$H=Tj`=(}xJE!X2gBr{OABH(0%xWbU{47sy&u_p9*9Bg_5a)d
?g65$h;9ABDG&A_WO$3)+ptE_te4r<Esg%Z#pf30Y-Xr0t0ZpdmSW1E!w~@HKEQBNHhSP>%YJK9`Izpj(!bF_BxEyQ_$KMm-
41<QB)Z7q@<Ej4PReU+7GyYe`B3sN|L{L0*8!LJjx!1gl4P@<ER|f-
7q@+DN1&Qc<c$f=a|e@$8HPxYN5Hvtt#H0jWjOUP@VCf$sfDK-
R>WQf?1c=G?X6g)oo4turyX3P$hGnG4><?wO_Gy)Sm`a1ALb!<gIm!JxPJ10ZJ!?cuZyOjsCrXnGSU@%#r>j~&vRITZZn6b8OKHy
I^7Pn8*l5_GwDkM2pvd6lmNl=8#*gmsZ}M(|NH+W*I4l;E>ZhE4oTKH(EiiE7|WyO@NquiVuZMD(s#IhlEU5g<x^^3o>=dK!!~I>
j6+0f4>z%!<Q{Hl2Z1%zXex!)h^(qU&eGMfHvr0Ca72tdsFQ-qhQnd+<7=vMldP&b|4r09t?ZnN`R^!GvqZs*yq#SLez~q9_vL^Q
gPmDI0!OGq*B@14pLm@Wn2$<}&S>%fZPEU2bCv*LD~sc%2Gc@%(YEVmbaa%hi{W|EUTn^Wvubq&#hasxtf<#Td3+atA7bVwv2I@-
VE~ihe@8ma<dKrfbpu|s0Cg4vpt7QZhKG-qg{b=?N3Jcl)T|NP2mbJ<h*g(mki0}c1_`9Xt~Tx1hWnD93I^9^%kka&eQZGJKN0^Q
%HF>g(sI^r8d!(-
j*qt{3krmK!UwOqO4KD82p8hFI&$5|vd08eqKPe3f{QIR==j!3X>h^3!2MH1sWV|=b}jI5eI?^33Cb9<pA}`%PN(o{NBJHO28h%o
67%Yka>a_L0c1dO)1xLuiL7pNF4^@YP`~CR#p|uHqj)W^=Z`|An4V_JnVU?Ze__-nHvUjoA`>v+X@&wd4J^z0t1l&!zg@ne9=q(q
9~2W4C$KRoB<<r2!2zB@O*ioy@d|K7Ru`M=MCx=!HzaIxFEbZ)$+qg9L=ve9$>}S{BCbXH&^sxjhhA}QBJ`g8Q$~;?!G6J$P6S?C
*&FQlH@`F|lT)`NH#`0?+zci)SY}qubDN!^ezhk%L-
6{AOd_x?m<U8txEW=3AxJmDeoT*#kFEDhO!~CcW$xQWqG7i$uF5uh6S~q)j2}qH&~GJvYa~Kvv~YJhgQhIlW{Huh7$ki`t;rJnL6
LhueDM-OiW{-ST=lfham<@`i0hq@v9ognH&C6=1TmeLq-
>R<s7guz0Gf8yo^A^bQy;u#ee1lK(scsO!7fD21}TU<U^!0tn{_N(f+mkCKpZ8ic;wD6XX2QP22>wl^@lh*9cc|Df{DC$5NZzPvv
}qLgQTd3Rl+Hy;p0Y*G2F^>5A-GsweZmGi<!<bLi5<=-
3_0phc|psvqRi4(oN2K6jmTVEmom{`96F(+Rn(pM=m^CNSJ$>Vo{s?9M%f1ssZc&w#*QcGY}NT8!QI&jtIZg)h+PB^($S@hsFF<_
Fdtai@x?)e|>HyEvNv-W;evL)xmU#@c`2rf)eUzUz|(mGTTBR%?f!0w+DTbFVx*df}9<J^;z&Nb$7%OW&m;Z!K)0-XgJyIBz%-
{bq2flnJ$kv;P_&)cK$4L<b_i&`uWgU7x6b7KkOJ*jly{-I6P$7+%<)nHRS9~--<O0SU-18C&pW_6Y|-
|9#I>q)MprS=oD^#b0~2mD1ossK;4EtFqAJ3@uG36Kvycr-0r<{Bj??wXLffTB8|t7Q;@iFlacNlVJ~-;Pu*ZA{eZ11@pPyRk-
b8_b-i~E_vR`8Zx!zyk5O_#`^x=?i>jqL+#{-%1vu{&W~)u}jQlkGuDoKpZghHXNr!|`HyzT%MG@Lciys(0Mc&fk-(A`0k-
u$iL!tM*yb+%;>beQc<-bZOIdY!Wvx{Dh9?&Pvow4|TlAiX4AAi*se-
8%9Oo@i9bjnK~$kGRpTzO^*R$|BW8j`!{?rk|0I+~+h*=vy=@7|zYzN0<Z`@Pm6slBK-
691=IGd*zYNvVjcJ4fI_ka@WcB$AA(xG2hbwp>EZUhk_>3)^CuE#F?|XKz=tjrd1M)!BLe7A#(G=S8-
x&ff|NzJ0qAKx;g6c)PAEd<_D5Hfx)=c<UX!$!0SlA-
8V<gSYZj;BE7&ST38lQha~gR`cp@dr_3HghbFk8BR_vho>Ji#I3;~f&>Ydc4TFt9D~g(v}J1(CRH7hm;POAh>7?NP!@$3h07!Luz
nD-rZWTF1j|KXd+~G;=#m5sY%XGUHQ<z!fP!sEa_L|@cmqfm$59j~q4_LQH4{RWq@PoBUW^YIRd|LoW&}n?x?Jj8!Rl&-
CrHv3Y~Lm1UJvq(G-M~4G6s_kSk$L`-3hpB^=-
06ZhM*F6J}BGIky6t699eM1Q{skv<Yq{k*7&`@Dx3AT4hD)A2%IcYkY3NYHv8;?M<}r#XQ@2*tCafmh6gu4ZA9t6?IS#>p7j@fU-
_GBG*+w_=_5FjjAM%B<6*2s1XIL<?DRP-
f<_kbtXn>Y}GshpP0z3VEN%?UBIQG&^no3@>2X2>~WlK+Qs1)40+%5&JKo14iwCZ(?7849=5ZqY5G>y7V62STnfhSI?ltCx$C!t-
uBkGa4;A^I)cIYxq*UslE<TqXq3m)D0uIw(X}#7yUTDZ6OgMIHrUM>+zauC?C?(y5C8u7@YmDf;pxX9QcvXt8v$`&eMyH?$IxNhW
u{>#ciB4pnT!rUKXpf}M{hp+^c34wK(vyv3o``ra>s%8-8f%-BKe-
f7PHIb*_GI=N?J%o*;Yv<*ii=TNG*>ei&e@MheRHWG?fw%qU2K%U-
)X>&!mMGuPI^!4@tm*_Gw8i(l0f3htmE2T20~soOE6t+&rLMg87Vr*_*#B9?-!r_U8%UadiR)rvJto-
i<YEmll>+a)sot1+9#d$MDBr8CX*9A6S;ID~IP(DM$N+jjy*+_H%?S7F34E&uZPlDYO_5x$M@4{23Kw^|?*0;DR+3tF?zHGBQ<;0
nDRZ{Y50jQh+ilw%$0&l7G5=Bp{b|+TrekXMSeC6)g<4@4zY-
x<(J08=qaZdE*%$pmNB=0$YWb!+DO(O)d*DdoYyEIF(Ke>8>R1_k^(|eNXDUu_ig}YOZ2T5R2g@ZECJ`fSTi$65L6ii51Y(Re{wq
I~Hrgjf~40A-
%)Zz_zlP;+vD^<KD^T$JD|8$(g76G6WbXt!o&k5_vp<R&BC~nT9D5j@;s0{=oTKbdw{V!8A&`eIDG&B>$QUJyy(%@hWq#oq+LyEQ
J(qh;Dc1$}-Ksh)v~ei8=8xmtiDdwCTmAklvehHq%o?J<*S8i{K|1Z}cg?*k!k1qe}~XK0iJ_#)XPsG(dE?bJFuK(!WvdkCJPR3-
=uL7Bsjt(#-@?RrA)Th65bB#(w$nqAZwWJxY4(VbRde1Q8EIPWAm*G%2E2t^Jd8Zg-aGPDWoG2Tu4+uKA-
>rR4@pXupnSmlusHpC+t;g#WPw=AYD50o}*;*L+#650`>dFGo?=PBF{mlzEttcV(&rDM<TX$5~zQZg9ufQ=^b<O6@}lj;?QJu5W9
^my=wrkqVi&9;6ymPJom2`QwM*eD`>`nq$)8E3p>Ap<>uptEGDx)3AMmDWfIL%P=<d9)!oMYQ8}spezEhB`_qqW#>==Sfdoy%%VI
>JRdpb5U9!<3f<A^uPafsfm-
KcCq#+Q74ibRSujL-r|Aw%`L%Q(2MnmG@O(!*=qouiJt5P3Xe{7Uo&79^19SR=OwdHGgo96WAsCJ-Ocwx%+Try7ML8ElG`=UO^6t
IkW8XcbTO4qk1f)Wc!beHlYK7<Fq`bz8F#Kj4Kr#n@gbRohtXcwsPC}2TFq~q8vKPk+Y!l#)W#D@LUO@FwPBX%Hp?A>`W&1H32C;
V%@(~woOKlY>&YQJH6L|W52p(IKRKJzYMf(|tD&3uX*WehVd)~hRintU?lGB3E*;l3H>#I`E(v;_I#Zi{mle(VtYyvTy1(uO?$_Y
5*NGL?1hHsO?IUEj?30gp<d?BWGQ$iZR`Kc$DiSj4qQ@Cyz??h&_*p%5?bi5Um4Y5P$kKh<;@RZ;^+iAFL9X8G=jnlHMASx+G5OG
^8S<S@_gg8%d^e!pKQxI51N`tbeL7EnHDbIjlUilZfdX<m3se%nHDgwY7Ui|*a)2Fcedfmix6O^M_hvDl8I~tUfar@F<@ftQ=RSo
afSq=KJuWcx=Zl{pjL41$;i$NF8vi6%A%P_-
g+V&gOpZtvwki9e{3?UZynxAL0tEmNFKI79S%|7v&xxpE+)~^QKjSnm69hI1eIBp>KOSGJb8W=7Aewbf|lD#d%1v6Z|f*M35beE6
V@L^1*)hp*}AFPixmG7zt?R;6C_0l^>nppdeAMvk}ud~^!%dDQ$jqz=9hUb~cl&d9#n(EURfd|9{G(&v!NGP3jA-
n@nq9oY4F_hA?qc36pA82fnODIH)2?M^C#jIub#?t^{6yY@|XJ_%E4a_>D(?&FG)^=T%G{mPYK*X+$U}|+p3A|}mK~4e=f7EGTuY
KK-&TED3`B$5>ZRGUIs%wV5wj83c6RA@Z14o1HnvcGLt3U=tn7~q4R_8-
OjipcvgoI#7PZE_FPN6?l^_45mM07S4M@5|fqS`FyC?|5xFi6Nm;@kxbHjy0-
C6aJ<GLfLXZppj3^skD66&w2bIh@6V36y*<E18mrzD6CfAk<j8-
d?BGVga=m&^|hD7L7tzeaEE9LMKMY&g1l^qXWSvvgKuVMb|(rQNJbC6(c{z-@6frFj}6x*P}^M2PlEA!F=Ey-
C=8GaJc1DGmT`41Fuc9Q#P_~`$kuMEr`5qMHL~utK3uImuiJwbzDLw(S`frNPj#$JoG%)yz9r9l@h-
SS?~{{;z@Jor0fmveAPcG)z7a|!f22zmf3kT7FE9a;pM}pPrZ>tNU@gnV>C#2UVJv&)UZ{_#O>TxE?<P~aJG&HCFlle%Y=&e)?;m
VZYiC+KPbJ4k&uOe+y{ptF+lyl6r%!wJg%+*1rO_4*TM`KMrXoGomzT|H2`5thChHBBQ_3O+$^njV02v=_cRPwncvn)3$(s@QTzy
cyF@{~(>SR_aGCOiVarj#66)8yq0NWgwyamBSO|g_oe3FdYRk-li+I@LcI0Qi>}`7uUE{*u6YExpIq{_Gv9}!fFoKs1=MfW`G60?
%%hRdLHxz88U&Aewns%gCcyI!n8;L1(t1g9+FDIv|Ty(v3kXkO$uF;3DT7(c?sz^oP--~zea?%+tWxI!L2jh4Kmn4A-
FGoEBl2Bz~$Jb8qK0OWL0aTU_PB?y=9CN3&H~V&a9Jed(L~)13baHa}&;Q}@pZ|}4{yz`@^FRLczyHtwgV6M^KONj)G8}W!v{2(u
eQ&Xe1Z~N}@|m;{W6P5DVNuN)+_i-qByafn5!a9{sVN{ZeTZ#b!}hc&#8@`Dzm<71x_8WNmOI6?+9>IvwHZf<L1|nEokBE-
@*WqIR~)Jd#U4i{nF}vLA*Vz34e7}rR8rMytW?OD@*WXqZz*dM&<`siPdull32KGDW{RHbj0T)Fw`S|iTA}hhIG^)+(*|<U1{Nyj
JTvRGC|MwtN@LffFZMExo!Aq=P}fc9we3r^Rc$wv02U*iTrX%u!ncu{z6+CUee&yJa$ugQ2xf($F*cwbwj*n<vNt{aK1lBJBWOzT
t?Kek-GHZCHS|xfQ0Yg)2AcgM*ec-<)TW0<HKq;?O}VXYe0JPr$9h)|{OKMX*lLWa9J>i{rnWDbeJJ*gBRn-tv^(tjpWv=fL}Eur
1-N}slp%eBO9Zhj;Y=#p@$k!t5P(L2f+AFO|2U+DS#YL-
9z~#i&Y)e0{h$@{8qkDF2W7#Skhjcsam`kfKGuV*ANx$C5_`fDL!p|@s&^NsDbOkCu6nHSwb-kKvvo19MCU%cKS=J~7x<~h?<9~P
#NB+bM#ttc6Us#aF%L>4aQ2IkFi>aZE0pLb7NR}NT`9Odt<9Fyr)|oQ7q@*N!@@wv9xI1PLm@LJp&ZDnDl@7M1Rw~1$;rx&n*fgc
gXEa+y(+cn)Nq3ExLL<X;eB@R{gouGM6q(o;G0C>U~SAVdR8@0>zH_&4;K$pz&SHlfMBWV42j#g;kKy_JKcO=vF51vBqhy<$rJm9
%-
Ps8<zbke>*D0;mFe1qZ9DI<f8G7e+Q4)&T9Y2uF=mgppK08{QS&w6aKle9nE~6;&O)+$$lp&k?AybotQm9eGt_mlDPILrlG)SSWm
^TE%W+Wa@*mnVC7u8QpY1L$!JUozX8av~^{eE??h_`b%U??fb(`0u?PCD`EH2qJ!{o;%Puh!om0Vur5cjjpUuUKAI>4&RvW9Jj@4
%HTfMT#h!4mi)!p-EQs0gkA8{5Oujljt9-w@c2!n`5Aq86+KQrtqyGTWo~55EF;-r>h+2X?IE-~IUX<&&pRzJF{-
wKC%l2kaSTp{sV&=tHTokBFwWTmoZrQrd2pi<BmVg-`fJ7^Wl2BP@S;WvL1N)Dsgph9CQrB7IoY!S=osv+sPyoETW3123w)D)u-
%cjHgoD{GtuqT1CR?RQ0~DA7yPfookuZ|1YC$sxEf;+(C3w6#qyuKC4dYbk33^DX)%-
d{*2ai!=LIPkH9D2x@Tmge50G?o|@oxRlv4HA{&P+u%So?dvdz&HWNLvRK6xD~}{LMTE<?55*%K1pS@^pr^^ltUZS?5Bba*M~R;k
ekpO5OYMfH7Heumdd{a)y!D_-8*O%16G9yR9y-ppfmGEinY<`RLRrbK+$-
BiTXHUtq;b@r`=(#&o?FXR0X#F?&Zs8$u$E38J@{e@4nd5LvD&}=kUF-
JtAVO0o-KY1TyT>>E^@oir){amZ!sq?4|2%^y*D0c*g3vvr1Jia3a4=ZQWZ;$4opV#91GU^jbB1bA-KAp5uCW#-
ANq0TMD&iMb++R$@6jpl~o(hf1!3(Mil0Om<%;9=gd)2qMft2SireJ%duk0@hZHh2TLEI-
^NA?+#b*a5`dERiohzr1EGJk8fWs^L)OHZ+a0^rg9**wQF_#2T%4Byr0Z2Sj;2EC@jY+3!9=Y-RHiFrs}DUraHy~KzIoVDSG%-
jlE2?PFI8|%D_w#Sit~PyDyp+b}-^v0T485(n;UCdP~j%CaP2|1ZB~?$Cecsj$1Ib4Hsnz7&Wc$hcs}*Lhk4HUAP7(bLZsF;O-
kVx0}7}DYg=}$(eQyURXt1y}VOI14^HA%NaFbe3F)k-@C7`bJ26iY+)omAA5|Pt;(IuRZ*UftTD(+y<LKH-
!5xcgkvCD#3uUkk7wx8{0SQDFl}juCQVzaUfi^`7Sh`Y|J}{B6$ltM{o3xUuFYG4gaNx)xBT4^$CeW6HEOFwm0O#-
m{_*wPHox7?D+8zneAsB+qExMJH^}`*r+n}k6m*=&UDONrIe%y3y*qXTNUW;-
@Y~{_WL)?U08c*99cOBP)*oFBDwzKrfPF(B(a1Nl-Ze70xIU*)fA1^8QB7rJz42yz9Oce`Z6NjZN?}@yHW@2XHw|ci+!jhpinn#0
Q$aSUekC9Ljg{%MrYE#UADQ+l5c|1(Xj#Z#e==10Tw~h<r%Ym=LsH2IRQs10@Sf_q$*jIYERzGqyt7hD)4XPz-
a7bs+G5w`7%GRv(<MHssCN^rjYtpnx^U%MA#N>kv9X1eiFnCg~>$=;{6X*5Ya`xTnny?$w9)J2_z#k*Xeyw&2?WTbZ?y#F#s#U^q
U_Zy_o*^{OSJ6=KEJJzkyp?-
c`dy#fd8kl4l?#Tuo)BIF(NWAC5rq@Fx_EEOKQo(*N$7$_~|2B54(gLN5nNs$T1)6mFchgcuh8)}GXXL5RN9$ZMAjo4jS;kmOZbW
}S7s!(W3QvIGwvUYcg5<M>hD7VNHWyGM)kdorL#Y^OiUK@}zR@cX5nd?VhwI2{!81Bp<e%EQ@AtO_B~HW#6~8NQyv>kc4aS8b^BS
=Dw_`s=(d76n{k>DPQM-*r@fR_Ci?vkKK-)2oikFJ@V=W+R?=RQoo2m4~V=#Pg17-w0mZhC4c^R~?lfQ9{R1Wtr=-
qw;r~c9SiWSsca+OH8+edY;4HH;eS6)^EE;eY1v$tl+@Yt8N-
gAn9dtA>^G3RHz`qft=P(WtlDD$_gPiF;HcNuREYT&C2slcAm>@T|StlD1f<7x+wVq?ut;?$|ctaS9x;~Vyy>jD0yJ<)q}D+2*ZT
bUw9!#aEZYC4xApZs-KI5wx3Y_9Ntgqy#~XNYa(*%VgpAbyYE0+l9a-
0a3`am{f?|C(5x*7&rq7^{WfpE74Lw(J{Ovrpkf8B?*W(s=VghR;2G>Y>Xl;q?w(=lvilRaM8gL~h7?duWUoi=q?yTkcqSwwHftI
IVCe8JI`Ia^qiVH+G;**25=<Z)0XV~gxa^uK7Tf{)*UM`5%Hkv(<Qcu)0S+x4xbLn>cz|69DlVQWmYwRdJGAlF#XPTeY~wYQy-gc
cG0PK~pR56~=Zx+Ej5GtqRXVd~s*CT?(hI>CAwST%C?UvUTZbAdKBeM&_30VWX@aaKHYZeOYO^CB;=3i!;manRSR&3j5VI!4J20`
F)qzIy$7Qi9+VR~^J<%E;xyBMyv~XcSmI!*)zv;-6woCt=mi8P06U0iXv4*qDIfl)rEVCrF(4^s-`-
X{2OOZe1Iyap)?moAa^WZ(lWOktDn@&Oazk(K#oewr7!yoi-hCi>*-Gd2VNw5+e1SciT-ygot+N>TWT6v#WIc*sb%Pw~N3@^>dN-
$@wH)qRY1}j+9NrVC`M2IY*fl3}edot|UAgIm~(}Lh;l3WAQohuK=HJDJx&X%P*QNq3EpgrL2yK7E^??}%QeMJn(LQpfVnXR-
;n^kl*^S#Vn%f2Hpl@7+$qhre4Pkkm|lOT(^2*V%{d3o)(qDiO|(lDL(z8V}>L;1(i^8r#s%a@I8)$xPl!IJXG%f*c{n@o!N_}Xr
UYp$nh_|gfFJS@q@c$rCCgT|#J*x%UzvZnDu*SOmnzbe<H&Jk=8QuB*F6Ud&W&{01lM-
%EbPZh~i=HO&%;FxF9PR_yruv|P35C1+p{F9rDN0p5yNtPMb{9qE+jExSjo(@x$7h(&Pj|CX3wsP~51tz0kf5uH(`J1*D`l>U`a)
`6Cxy<WmK&^)|&H~;|5(<V_q1(tTe*5_Q$Il<WeEiMy+b2&SPoF<letXoWG!yeNh)1ro(~bbO*kRTEK@yCS2Fhj(Z;_WXHS@}!@T
Z@C>P^i2e=G>#PG5%Ni+8CSFTx!T-$Ft72-)Gv8Tu~v@Ri0i7CT8R&A){eKIs~>=YnGr-
f9~v(DCwTu?Lb}9Si;Jx_42brsHLMwayuYHe9IbczMyTmiQXK1PaU=st$jH=*j+*AB<n%Dw7T1mrw!qKK%MDYcBA;_!D^D{qm0l8
vX`eujcp`(nbbeX7wxBsl!EX&=?PtG?4tx3S$=hYq2QaAWdP$$)MML_d+sj9kv39qZ%ZfWMgY-C*U@^gT&?o`nbq2uA-qcN5-
yJ#VVfy1uBlEvIED0m4U0MI+oWmKt782Eo0ge^-K<{n~qqcjjv-
)5wbD_p;`^m3^{if`%@lR#eroRSZDC)O`vAznYV_5>n5~VQkm}5c?gM2-
Dk7Kx&N$r?LAvoez`Y+HUg|8#4iG?)Loi4p8ZX2m}H??)J7noq$!x;dm!hQ5gt62*V&GI@=>I)kl!q79HvSx9A4&UE0$~-
4&&N<wFbf)zRcn7?ySE0M(Jd|b)5@fW2Ru@q2)BiGrD%=2AtJ1MatqGWppdb^`^ZhtQ@swju%hz;wg^Da9y6KE@0_%jpKk$fR3hG
S2L|n;BXh!5U*a!r$Y9E*KmFU*B1mFpBIbOI(KOU-y8-
vx<i)+5lIMfuV;bNuJjQ5)r?${#Fux2ExcX?Hvpk1=Hmkh<GXu&@6$nX**_Q^h9IDF-LwI0ns$yC(#SzFqceQ=<k{n3`Mj=oEAM2
T4n^kJQv^T2ZU*r^GjJeZZOQ^tXhMQ(b+&x>elU}-f+3H!@$A-b4*{bWh_A2^E`HNqLCJBwTcp9r0JZ5oX0-
o{adMpC?X@jXcqB7n7f_YDMpVYoC8BxXluwr_NVfq))&Bhq_{tTo9fvoNwYkUJd%VFxg)0rLlr@k_#_>%N3Sl<8pbJNX_}Rq+SrN
-Qo(%A76z~dXe6jQO^BRsdHJEe(Uqp`&uuob6hKni+h%%&F?7Tq8KV9c2RH1LlKrrgk{lUG60xvPlF%7t9j8J9d`!sd$ra(^#1-
zp-3*8+#_mnK@q`WrODTy<AM!1CGB7_@BI7encw?|Y2M_?4flr0dOC_#4D9UXRgsWWS1xP%e9$ip;hhE2<TVHo-~2LumM!5N-
!U^9a6><Ws>F=f~l1HJ@4B*^lpnzea*C}=;=*uLEqe~PpVZ+Mf(_HqkNrkI8ix`K?aH7++K43DpMKg1J&J-
&v2x7ev~b(P6Z_D81^k02107_Blv)^@+T^YZUTUh3LO?~;{U0Fn{aT=&pJ%oL9Bjo5qM<PsRLZ^81b+%S7=zWXB?f=W4!eCMWH^c
4<HP*6)AxL0#bX!+xP97qT0X}^n;qF)`b-
L|TdC0tYw_x}K!guf4;{0474M8c~|v29&q48d%<ndkH2yZ0ol<e>!bX?ZB=Ij)`|nV;fVyjy6PnvJr$e~4Xs#yj{h)H{zhe4CH@5
Z@bt`>&ykDOs_NSni95y1wCgqa-a>Vv9K1QUk_76b66a&psWVefB9vMhc!-
<6tOK#~TaW!yfgy@t*q9n@vpLLYL$`$(a!hLtSTy+=HgJX^R<Ldjc++G`?_9D<}*4=8{$TMCLtCi<*-
iXTY$P{l_0y?S~qE!?fk#(`eI#{02kT=z$(`T+--)SXc0>7JLBCZKSUf-Z|>zF$%8Oo}^03F*Yw?@j9z_m-
!0M)sFMD&m6t${Md8Tu`x*gN;U>P?8sR$MMy5z3nmRv6QG8^@y6a=1a><=ma?J%e^!)PeI>o1VGwp@;`=ag)RWFO#d1DH8%Cicvm
JGb<-izh*F%g#1;-
d~w*?Q80KuV#b|gYUztMs5A>g10U8joKD&ZdgjwGNPqbN163NZoBF(?lNh@!^DTugYw=+{0`jc${2%|&iU0k!g$jM3U^A_42Vuqi
a^fQdz^&;nQAh)KY|p>;U8#(_A1*9WJ8lX~^JxgE!h+?7L9$WCqv3yi`!y%EBkL9}lle95Zr0X&Yq&^abVHm7*>2W#q?TI7Ogb8s
Ih4{`M5Ql&&NLVgtd0RteO9I7h-gm5X4TUQXuiaB*ymLEdGTg4I&Z?&FR)j3}MB<RRpt2|{yWbv5=x^-
!?*j@=37kOAGg+)h;OqRXjVO5?%gRe1#wYzFepbHXoA8!evM!I)WjS7RHwfq~GsA4UV9=@fieV1kd*O}&1xqoe0Z+u7ecuagrV_n
$-Rl^@0HT;zqe(Dh^%`C*K>M>8#o6{K4{{L}{*=aX%7`}n7j6rwq0F0X*xP+LJCZE1pEvH}tQ8B&veS2DctUT{dP%opG2PU}MO1-
FZ#!pWtCzp7VKc1YV2dBNsAK=fOKK@E2O7c9<6O9BGkbGGk@Bs>N_B7m-
c{9t_xsD=t9BvF<3J8%PF|mzF%dwpVh1r4CSrc^LJzDy=6hkJu))6$ePb^r(B9CNeo3#W$FwTb(>l3jmu?dUHj4Z@`A5nqBmt-
H564K9b0;Myl|0eBE0@v}eto8$|A&&@}978b5GG9)~HPPWmh6_+Bbo@6@<x;Yjh<V*qn|hW{<tc-xDG6xc@-
3UH*cqpM=UUmh#K}j-AcmchVcUqMOcSA>la1SZ<vm6hNUFdYsR86zcE}|-
7{+TBo2l)aZlq6fkhBI?&t*|tspVtN&mfe6!WjuPy^=J*b0%EFfuqTIeU&$UK5BmS!&~h<0g}C>+JMp?CVw>w``eB6?Cg065TdtT
4fz&b?rbM^50mgZl|57@rT0olV<py0v0TzaR+4$jtQWE!yJruWeFd4XMuED9j@7#I*=7NnUp4$1M*YbT&dIxYJ=FfHgx58tom3^n
K12BkL$1E`lFZ-
&6x%Vp_@Kx0qQzJ$6&)nG)>!@>kVErWwdZe^dff8XkE>R<ueDXRM7LwPX~NeL<79&<<3pAwevX_@=wtI`p09h%c^O@g#|gUFZb^N
iil9HRwUp&0D7c_63e0PNk=MDqqA?b)nCsLCi2YPP?eQ-8&egJNXULQi)2M8aYFCUTy(1%82&4&s;hhSZ+v9`vpicLcf_t-
)gBt0QdW$KQfoDDZ8=o_5!a_9Y3Bh^|HG)14v7WQ~P}kD;BiqD#XYv6n#m)!t9N#U6>P~m5xLMs8zHf%9m#PRqmGK28ihA2tNruC
9(5O@FwC~5~QwvkPWmpmoJ&MFeT73wOG_3&7^WX9ICm0cbe|q`BqWZmN0zv#fE?&_7u3`Eb!tP=E>i%aIs*u`loowyP$rZeaQtgt
C=;-5N2{$>b<|<cPj4>D)7cxk?GOkRzXXG)JDuq2V2+}KPG{i{&mb%2rx#00S)dHS8wsN`tHm0MmV8V-
=gt`%q?AV<XdG0d*dYnjN<cfmD+!F*j?tW&M7pOGaDP5kRbxQ_iCqF(JQ1V6K9YUaLaKh$Ud7jtRra6TDCpj0d%JX1K7r66!O3sy
#BfctQdYU0a^9<JyQLBE2HUsC`vN~s%hq3ywIa&c3%!r;Zvo+dD7DA?KZGDY_xG2h3kgXfc#nu&Nu?o=U9LNCOsl|J`jNYs&#}Yv
jtV*?oyqRDWf_k$no5SIVjPYOF5~#a6*5B*`IBsM7*M1=eZ!G?|AIiZQ%fC)r)|ia#p8>RBG{*XyDbR6q%GsuEf!K`Jg7g6aMeP1
uB+;oX8;grqpj?&mB5N$bLeFSJ=Q#QX)_H!mIgf-?{_rp%N=F(`9)I)X<@DPho_{yO5g7j!ran=a!cUyS=`t_Je-
(;n&|^p0mGNp$SzByX`f7K-
V$2JaI1co&N6EewF7oey%x!o})tJIeb~?DZ#o&DV@afa9A3pm16h_G&Ai&QbtnK3yp36aK?sp$D>>G}l1WN-aP=n!d;)!>1@Y*(7
9vS`ZqsPx)KKbE$GfL<Xg=50|FIwvIRF3oqjj_@ci}cucduN14&GDygUayK0lew%`8RR&X$5!|&7EB^vqe>{h?slz~f*TS#?c3(?
oNm_gh{TfygAn1QPQu}tepQdwnBTqhbIS?<XZ1<|IRtz7>77ZvIHhmm*-
`JS(Mj|6FW;Wr={pqKS?}<$tPa;gf6MFF`C(mE?a5i7ezTcZqV#Q>U%gs1P+~ZtfV|U>`(Fjyna@wohIdZRs>S$dp1(c{6zMe=n-
+{!Z|hvlYWsE#Q&ue&Z!fZC+Yf+!aMIjCXuW2R7{4uFukw@m$EEoH?Fvpv>LZS}m)#SR!J6<wIYR?A$NJh7cnad8Kbf3(rLNRS0|
*mm)Xk`tpdf|ksgNL<;9x}O<Tlq~drj|iGq!ptwV$5GciSSu*fT9&U^NOyquT;>x%F~$UX;2Z=A6JspfzGW=PClweyC2|U7P^usb
QNry@DGA4O<ayME7uZitR!L?bS_|ttLaJKz6HiD&STC8+_ap-
97?=1mN(&(OwE(3qqh<3yH$NLseqVs_tqyU{(G?&?iI^GMDNrxY!=Y*qUSZ+@D`w$rYa1yJ2Kpg8_jM-
$)nMz;t_2x=M3|(Mbp9C$RzkM5f;2kJ_ts;dx}H^CE*C7cW&>*Ldp?U0rD&<BDk9r}73(`AA`414ol(Q7#}=E&YJQ^kP=5v$AdU!
)z{gO!E_xYZQ3CXP(KN5MUvfS)S~cWblL<81@sBUAfQDXkk5}tStN~Peb8#jKXe)RuB#%D_@X@GkYQL;enxJKVh!fPjyY0+ng>f6
U{=EO<OD>4`f@t%1bdOV9sKX(I5PxTEf92e_jjn#A^vxqJ-
a4Tg@vmABYrwr_^}*CrXa$2e&`t?`75G_Af~#@_`@{uR*CD4M97yVkg;Bvo4-A>!V{w&~LhKp!N40bqOs@-
)1GlWz>)8E<&gLigCEk33{{Sxsa8#$4x(ul}HxytVgqz{|r+Zdry(}+>jr*-
y_0Z6y<N$kTqJ__T0y3MHP6;ER*_Gqt;bu`3PEX6s76khT8NaOhaZp*_85GfLLaAA^3}sz9U^!()qC7(AB@{w_rf)eC7pCL$ckWn
u&q@Et8$=-*pbhPF_{boXh!?Efwo|3*ijbW3|H6Z#5)g;6nVk%<4I>Ah^8M3>+nImbnG9&K6!*<&;rB@rQi?s~?kx&y-
FYormbW?I9~xRgDX5xZ2S4vPYXT@bD}vy<+$*3i(w*WWpYSpHk(4p67vwIA~GWGzU7>TWs_BH@9vGD8xxaFXdq>)=|%J@3)?uRju
{gb~CYFNqJ&gl&=e)gmGVouBu}I^90i)T2J^e(L=$<6t|XQ1~ekJ$I|Pelu<xJDPD8&W>fml#3p6^?wkzR>Vw;w+_4#_P){JtUI-
w3+s9n>bX4J`HvljHp-Oo%mCg*#Q_Ki124lls%JnF;y3Mi;vP#<4q;wbOl#0tS{-
GAVy@nVC$LN+*hnhGu)J%RdgQGeW6Afs87ZSaohcqY<DB;0ud~hcQZq*%D8_yoX+qx*uFT#zHLa7gFq|_x(=uyyNcYHYrI(rwKm?
1Rr%9^W>yi)`z!%S^;aj&BUTf^@>PPntrAwj?nfD)^e$u^r}K7@Zh<p)p8ssgQCc~9U$(55WGhz_rq=(X60AruIzqTk~02{Z`)lu
%kFf}o=O4tJyUTS6dM1BKK)K|BEp)wH!VsViDGLd)s^znF~}E0H&;U5mUt9e;w!=<XNC$ESUFpf!X=dacHOcy~dk#qxorjMDk=@$
fkHK;bbKKsqV^<sbjA<l1WDrr83L`Ey8BVs|OqC?6&yJ!;@oh25Z7-
DvtHZfkg1$b&Dl<f6_O<CC;K9~~WGg5<A?`S`QryT|vA?|y#oi_bs*<nv!2-
~06^C+UO#`XB%4zyI<mdyqVmce;LcQg%SN_sQMQKe_kW{VzVf|HUVt-}^N|_zwu-
C6IV>4V}G7{^cM3S3RCL&6h_ELD7Ku1qmeulL0$dC+460`qR(85ZM3v{%7~T`1BsN`+sA*U!Fbq8*mW1giDUka<l+qGIP=DgU;TF
F}QdC{_)-W_wIdi{Mr4_1=N4}r+@e_|LGqIE->8(*F+3o9^o&mBg{=q=rCd))RdUDshp^lYq-
0^zzP|e<>YJ{*tB{dIG9W20E;4gJy~Sj4_86j7xnm0w!aMVY7{qVhwLV5Y%<=umtLoI)jNc{z#TRAl}+ZDZsOd^28-
ltd^@CY3IDWX$HjD&H&Z*mgMD*QM~!|cKMXQOwV_~TI&JZb3e}|<_mE3U8*M0k%+)d<3%NjO3$>d~$Gw5>{S8W4?Kvi@!uuQ&v_!
<mgf{E=keqhpIuX2a*YjELd=m)xeVuPcPR^)_@JS$i)FDPV8Iacs?Z5s&s>lH+4k5bj$moPY@@u&9RZs=|jU5c`oMtF^649MvCRk
+w@~7*~vPDK2u7xxt$&F41d=C?FEuPAlEOH6hOE82yFSh(ANk%$*;6E5M!~{Ou6;>kyG(t99+c%*{W)S9U<wK!y18oNO8dlyWQ_+
H8=+!IbSQ1+{974zH!Dthylq`$0Aw)0>ESjF4*+3<Oh<0q^&CyZ`)>0!L4`XxJZM2}bp2J1`^A-
5$ftKA6Yb845c8_W3y;CA7%;_@kaile_E;F*HxXU{MK9~?%-I#}Nk#>D*=6#Y#qtYy^R=2qCC<m8c4g>PWlaAf#z;iY-ZvqaWlF7
;GaVf}HY_)g#7U<SZPXTWy7g_tHlp1%!cO+M&cM7P4;430nD#*y?9vkCs(zpJXRDgjY@23A+JHuAp*ONr1o3enIY4?W1m;gtk7}(
2$Tu*Vk$s`~gqTdR2LLHphy%|{YSbyM3qy5uByl~qt$3iafU+ln8WiqsC?9!=vq1~w?LWiD~EnZMoH%E$O!2wFWS&<tZbtctREq&
$0>uuL3H16e)@VPaok(9A&Af#vZs^{eK4>~Ku1ukAzPc0=%p->Bf?~)}_wgf~hn2f*0ZCT$?-
ERF><HRL(GU)eQjw*LL#22)h7{YtgQ1Zj?Ei$5}Ffwd!=R-
|unBq?Eo5LyH#5?uNE0K&!8u!HQ1>?JACv{spQ&eQXwTq%Xu*#j&8eZe37$3bYPK$eOJ*rZNjuG4kLi&a4B#-
|*6&sE1Cy$SD10w&iLnK;YqGA_ACmEej2(Q}2>za&@yh_up3MuVvn(Nz<afn9A*IARBWfd?tOAm5j$8ToQOU9WC6O4S)<1AwkWF&
pET>@r8L>8JQh>h5sddwesnpxJoGTp17;fP+Q3ORb1I*tryaA3jQ>tgyUzlvM&ArT)=ax<-
7i}5Ys7CjT(;@k7x04P0^AU0FJ=mKmn@U0eOfVZ-
x=XLc*JnhNzb(80KIQd2vY%fHau!|oT*kH(XDkqh8#$SaBAAfbJF$<V(Xp{m~{LvW)p2gNGA09Y6qBJ4l(<8U5RMzj`FW-
x;7nGmTbx_#PbYPOTjZ>2a2r4{#{=;8C`R4KS7yZ5;xn->gWM_3QcF{7Qx%pInv9%%jp%(?_1-8&OWQW?s%A!pME^=$%cX-
XaEoG>!M;rut@t}7M$qC9{(8#7IOV<LYr+l@>v)=oZg|-jhEN>|&AfTK4w3io<n-rAt-GkWN#S&qq{1fL3oMysrqbn;i?Auot&Ou
0M?G{1cBUMtJP&Tql!hR=x!f?nRjGZZtSX5xK`>aI*`FNb%4a|v}|7CWD9=!`q97Fvwxt2g~j;?J)0-
4kx8HZX^+ueM1QI%iF!6+Pj%og|dCT^|#AbyNmJA(c~AC6_*-UlDZ?7YKJcLPy^Qg<mcHINz08SE{IyG$@%sw-
|mN(J0uwxHpv5;Ikm#jGcI7~`gWIjQm|9aV>;nk;;F57^_MSYVW$^x<xJo5S(z*wl2gu>E(USm3h1Wo^y4AE`J4F?mVcjb~HvQ6W
EgvlVrf-
E~u32nFN<4KdLeQun3<3hs8l#_vBc5}R`Bl@GYrZ)n4}uP6XIhb*`GP8S+P_xjj12^46qf5AdLb<mUSN|Z!>>~~f5>XCb8gf2a{s
nAg3nErULa7f1CU6oVenE!B!F{&QNIUVcg7zU=t9ypwe6X%%!a2mErbL{-K3mcLfo38_Z1c4mJ`kP%~-
>_gLoU!?8iZD~M;VMG4F9c%5SKv|zcK_acSrev{%JWg)vNcXvdogdGKyAH)jLqP6l(z>A4gswPT{ZO>LM{EnuCWkW>hz+*<14;d*
PBwsdcj+v>QGT^LI}B5Q=S!-f$fwptfE6Ov5|GEOW5(IAx#}P(qJePlhAeu+q+l9-
^wtoi<P5=M9Ic@?W~F2oEkyWs~u8=d%?;!X$=h33>;b*@LAUI&+<i8=QMF!Cz%(H&oac%bEs|{7=I~;&~xOl%5=><TV!gkt-
7(<4ipOHhYgMR792uV9Ka!`5etTc91w&Pu)@fKrYyqgtP686O;~PB5_%&qA<NIQ_)~7SbX*ZuS9C3wcD`@TdZ2|u-
cqP798S2W!NjkuOZp?GEzXx&4F`ZBo3k>-s+d#VKqBwVHm(0v^PA+AkW0Y`8?-
<B$OVqVf^WK*J?p*KXQ^51DU!c^S5RfFu}Nc_WvZ;8Qpzt>B5_6<g*`;!m2-
ovBXrqx9~Hr@3^;Bz{xT@z`!(3hn1t<Dvfl@UX!L2Umd-es_j{T$AyPvnLDo|m%#bXFN<O$<mkD$LcCz~i0UPDz7U}S0T)kKnMxa
KW12cP?p+ug`Hx^luz{{ZAX|b4=c|OnQJ$=}tSCk@h)3&Uo@l{YD@*I;Dh8z}{j${p@0Vcmq4)2W&#de!by#x@~X<aQbhcl6xj^H
REO|(mzI_yHeplQ;x6_m02CR)PLt5*4nIzl_4I|<Bjj!LTLLZiisIX584@i0lNyE@Fkuq@UZ24>xy_vF9_3V4lBq%&`VFM=EUo;8
m~L!vt~keL7`s>s+K7>q>s);g&5;cp**|8n}>!@r%rc=`C*izN9~@(?1Y+I%K9=4>g*Wd%Dkc=>=vE(W=P%?dWf<Kg|GvGf+@Yq9
-O0I!gA1d~Qt-
V|UGj@><`$)RjzJy4tPl%6idD9G?A2qWLRW2C>;g%b^d4G4;t)AzeNh(MLxYOjes)`Epul*XK5`%{`tMkdUi0K!p${2D2#JIboqN
O|jFH*JgykSs#8Lt?k#yCS>wHYT&%h4vKM?aDE!Jyhz?M{IYodndWwop=vN{Q~Y$bjii0BCoDbc)+B>lt+)vK*dg&Vn>tk3CqTIg
O24Wbh5OoU2L1x$yim#=IgBtQ`~_OdxIVu9@m4Xw(SfZYnMyIqt%Ug<kk*Qde+E0!Z&;brK6jbx+c@l#y~fxSlJ|E>=HUxZQAvwj
hk83Rwgru=_C#m+<-
nEW)LQ$yQdzHcz+ufd~UI6!H2r(&@!Y>%ph^S9VM#AD4Zb?K4uuaR~Yl*J&hZF@oneHR)nHu#cfoLJ=xvl8t}msD_jV3XDZ<&4W$
v;8FkRBet1<$N{im6W8DR;mjsFTAyd8jC`5uUJLV9FHa?H=3C|^bs59Hnv2EenU2*}&m^DoS&R1dwZ@?aG1QY$n5w$&jaT5SbEh?
D4;l!4H{P(6ke&3wip*{rv!Tay4OS}+V=yr5i++GNoLP*F$KyJkbGIZLoQFev1z{vD>s9^f+(4)49?t8akU@F1|*>D+?6zT(X2u6
2bcMhcw*}cbb7cKYCh5NpnBmtlI>dCgFOo1@A$rTdb2j#+X>CqMxtWA50w>3d*WlyWI{Xb9gsHp<xoZv<+=ebUQ&2jWoVcV5_Bwc
plR0w!8coqZTlS5gak2{wBZ?vB5N$Wm;Rw8v&PVSVDF-
l37jbvOz&oJGDWsX6)gFMIL?Z~zatnley(9RQd9kZsuTye=7ptK6~V=}sT&%dCYAr@@-L2@tdniXd=rrB_FaeGQcY_SBE-C#!1-
g2?x7TLxsYY<$dY^-
l^r|zu!aVWALCxGIVVFHxtHFk?Me8RUghDT^7lXZA6Arn(+)c4+Yj|BL<KQ0WPT{tm(ehJdq%HiR&mCNrn1+ca9S*U6{xzoN<L2&
UE$btE&oYi^u%I1PG^Kw8djw}E0*}(wN!D`>Th=Id&J2Aubct1M;d_I&O*=-
lV5?j4qJ9cXcV3!>md%2$js6V{#!CnBLZKeX#)c)oI_;i{Ka3H#;8$Mg696s@BH=W!y8-
XijYIT?n+jg@S5dY{_w|&TNet_k&y2NbZT!U4Lt1F8^f_BUW_7|R65?Koo0;Px*e|?@3@FmwM2stWpmxR2+`yBkz1zTMebaRzJ=&
ITzaO#|_syfGZM7u>fTW;ogk|hgK<07#TO~PA$s!bau9E59(lQZBY$);RF+wdN29&{I1CVGbqRXoKQL^&lxzlng=!Zzb{oLQ*>+G
1F-VR};+v{Pwhx=kqX>9`tuS5pcW-rt-Ox1zwO>#plxCEr$pAt!JIMH94!C{LJbxCfXHbx}Eyvi~6-
@yc`GOT2zJgG{qS4YE^^eJ5jFg!W&w)jHW=cqx+iF!^oqI%hNokPjExi~>+mJ}Ilq0p-BYbnIriyc))6|C<Ws8M&Pr+F#^i@0}-
@A5E;Qzy0p1p#F35O`nKUc&k4JF_R!Wa{U13QUAtIqSQAO54Vf@>aG+lZG|4cW56mU`^O0p#MMk?_C3rtg`r<P?LO!@mgwLxfxUN
+wt1VLdhAJ;p5hIBEdM*j<VnsZ>kpD+8HJ~!zv#tw`_OH9+ZKg$>pIp2|4zt=Vy5!f1>BCow+&=C5ZrW?oaM7jw1}(RjDB*qnM1l
4EcfO@ln~?=ThzM2hngn<U3_tT3<48aU~;;|9X7UM^2}uw-
&c~~#KGT!BdgE5+tuLn!6F~`u(KhoU2JU<?gx_IvBTkb&EBWSzy55%7w4Vi-
cGlO?aqj>WJmP3ul{<e3IYXvD@+494RO(E*H;Wa(;|L@l_&@}CoR~Zm8R(n0c)8<Xl|Q>o-B1Xl;iR@`E1id-cs7#5FP~wEQ?HVL
QLe~pe<VInY&d;%Fgh@NrT<b4YE#<v#RMbKhI`YGS|a8yMkQw{K`&nyK+NYbm)qAGpE4lQB{iBZl&;gnf$vKKYULe5bL9@W^j{B*
;WZPOsdWiissPi3(>zNB*ox;Gf98Rn^>Z0au8DfN$W8tGVe$H7&xsM;4-
5$^J=6i45v)6uHu9oNK?9&)WQOu6BgI@WgF0xNrs`S2k-G=uo(~-
F`cQ{Y7^e1Ru@^>;QhHWi7ai@Se;4yc!9$keq92+)z>x9y%?0394(MROO1rDIuka&Se;Tuu~(M2u2sb{Ps#kTGH}D|HjCHL@0=?}
I-ON8)2@VQ`VvlMD-f{TmV*o~G&shA6iFeApMCQa<>*a%KqnMUHlUU1-rWTsHIlI4hx5&9-
KhG4?QX!KubCCam~yDvawOyfrg#B;k=^7E+2Nla9{&CD;jgE|!&8{?X^MORXD58MtqP)-@OJDo-LImKDGshx^_y{e&GQgL+cF1nf
*F%3=ip6x;PG>28PXRwV>5j+Hu8)(5Ikj=q+DE$<dNz|He`w+A61JRK7)j2sPQpANB}Wu076Krg?ebzK`=zB8*LRpFI9sACFhv%1
iwFLbBtdS8RTt@>@{AR%ea@J(NiKud0F;EKJ>2Cn_!x1SV}5iwT5p)h1ZfBp0cTd6xkSOU#yE<nUP>t<>XxC*__8?TA4S*NIsXFy
TIpMpj%&=tu=wmA;g>CW%a5muackIYCIecf08i89-
RwptEPc;IM%GJ&?ZAGh3*Qh)81F3KfFC@`T|IA@`sb=%hQkhslv}a@{@}M;e>BC=li_uJ7x|M73lhq-
d#P{^6x=<a&X{hVv@3h=c|MJDBYK%*!(DVzfP>8DzHyQOOk||vCFFbD#LA6tS#3J9I$R0g|LW7?<Ts!X%Ng1Mdk*UD+wV(Kev*ZD
*b(Of8?zShMI$?FN^4_0nDOMN7%GD*g>|uSW;ydHXJJ?%h`PEF~Lk80n8&bjXlvz15-
TG%0aG%D+ibkcnK}B!J#oJzo^9GT2=z3gy0;Sv{F=~N#<noA=@HZlgQZflkUz>W)=jKs5f*yEr`SLTdXUgtU?lC&>5G-
D<<On^yOQetG5rdN$|_J@=Bez59A?SCU}8Z?#Y*LCF#C>a4mk{h?1i5w-0_YMz@!c>l2a0-k;^|WiEKbPps-
sh}ciMG9;PF5{iq&fpht*5c~y81X+Q^{@iq{f)G?Nr$I^+*vPPHJV4|#X6!Y1TGlbqwp^obFcmZ^xYn~TiA6ma-ubHk<%#Oi$=e6
;4mL`BBiNgG2`z~?Z~wAyS_j@v3=v}_heA7oe8jc6KUF7hOCjO!@S7iAK79JrSvm^=`7E2gvagGbbAQeWQ|dwLrpiSL+A2tra`4b
vvgDwo8WdUho+jNsB4PyGQWq4F?M?#$0SdSkx~h(OMtV*pDGnkeIQ^YFw4bW$Agq>r1Bo%Ys*w+=jP^AQtRK317%8&S@^b<^x2I%
^SS-Nh3@Y!&<n~-9NF-~_Hr_K79MmXPQEP{|mUkqC-c8({V|QXw@M3qr{;SQR#RstYmp}aQboxlF^(nB;>GQ{iH?RS9!^qr4d-
u;|z5ZFQk(j4hXpKZgV}61|j%+CU!lpy}yG(i|)<RY)XApA$V~NJUO1>>>q2SCe^4TjeE6o`kINbqBTyBXffTe*rR!gM&>R*eh-
V2d1!__XVe4EM2B_aav9e{`F3SNQPgF-(;CBUcw$0Zu8pb5)C#4%+>ucHp2f!P5>9XSMmI;GRo&-
e|i@!^n|025HqcW&QwmL!5*+5#t(`8;PK?vedTwH3Pr0<oCPD1-|LO+yAlHpF82-
VLX*?gO}vZleWxoS1Z>2w%4hwZmu<s+2Y+S^z$abn@*F&%b;4GI{*``47)elfSDr$(o;T_nLmvyGB%Q`oZPC^$h9dMShit)sZLP|
L{@^%){hyCKv-YwAu)!bCwG-ZW0ihn|z(YHIB(oKQWEsr=RFBd9=*~Gv(E`7QQ~g<$aQlPV9L*Ne3smp2RCrh#rYTS9k~qM_z}>v
*^Xm%`RxYSJW5jHAns$2trVZ`0vKT9W|qy_k`eca9_m(L3Dc2Q$^?eT?c+<JIpSpXoQVgZ+}toO{1fBa4n_z7^`UV@NRVL4bK+DV
8g?R4K+*_y1@jnLCd0b!8Uw$PNs@S%sFhkU@%vfDt*P<30_s2r2Wb0{_(NT-t_5~f5R9^Igl6`&=f!@>$}dcsTv;3zc%{s$+)S8*
|lj#bIOJdot=KWv91en)9UQ!d=_#e{=o8wj)lNWO~Zn0hZFPOCvO_4x=IJbI4U@}?)i1YJ6V}$b>6hrE;uh13rIE#N2ar71vikuk
`qAKsex&9kd)*5;=!h^7K`!m@YDN|wzAh*vBU#hYtPkyCZkV|Ps3F&3gaaonsw@h04l$Y<zLLss`}{OBFaA@vWjwA*0M}?)!}@i$
85ZVrz`Yx4F7aE!>Umn>u<X{wz8ws9R=Dw&t}zU%OXV>Y^4rDgXC#<K_jm%UIsP0olfe*QBbb%YUlOfS|<pO=ztGkbPnJE!f#f~_
hgfn8Y=UP02e@I%OX?;NpW6QFactM=S2x--
QT_Z?&*>877RNUn33Qd<hHh=u1$L<1r-vQSn@!JYUzhfxT@{I`hCy&{fV3KB$StA=hi-Tpx^HgTn@xHCFefpE!&Q@XB6yAH?Y%M7
L;BHe`SNlUbs@z79*rZ)bD!{IxFTK)}Yu0W}AGfG)fNDNXCf#Rtm@R`>fW#v5iLHGrgO&N8W7OZ0ZGMlP&mJ(sy)RRLy2tBg9R(X
9tgc?D^*^kM-hO8o=EXL)sHY*JOVf*&3X@wSHJ{N=Jd4t>#!{*?_ht{&TUgj;!QaPJ3B-I!^NPqG*y;-d<GmgeDEV`-
LQ8tN}!dde-n1=t}HxIX^MN0dHV=Kuq>P-uVC-^z-^PI&EJ#qis-ZffC@jp;2B~bm6r+7EQQfFMz-
q82Y0(W}5rqBPp4<X)gvE4G9ZGgAsha+JjXCjw!oZ&PamjF-8%Uihq?nT#C6tdndWTfmaF$BFZBP&-
lQtHYR&Sy`zG98XvOVOqF_EIt+BC*S6YV>~l<&*x5eEIvVXH|M;PY>eKDT!aopV;l141c;_j+@ImLy)tTH+;G2vvg0G57RTGhexr
K%hFz<DRQCo!GiG{zL$;;UM?d(IzXC^A+H+WWlgzf~|5fmKGYw%#R<hTaBtmi}TNPACVRc(wx9}g8v7~LKzJZuXBp2Nj2j=?UX!j
3IDl0;1Mc@I*LAr%T6f&-
!u(LfUAH6^@M9wWuFXs>o4jrSuysl>9{jb8TIzK_Bz5!=06vU4vW+xM~4Sw*AfOX)!+`LO^w;f8}*wZV5L?*lXXLE*b2H+3301^_
UR#eoG3UyoI@p(9mjF_>y1Xz|fKG`T0PCGeZ%PI8U#Zc<9I3ZNe(cO@NCDH}yI9Du3Qk~<dfv28^?3L>KwO(S^sb(~Nd=UTrm65(
X7nq<x}E^&(gJydO*&H@7&zeK4M{bj|vTMJna*4=|I&mP#$wcMC-VETu*4;}RTH(wr|J#el23)?|=c2W249`~i;OZ9>3Y9t;Q5Ij
sF66_@-
75J5OfeR@~=}=>Zzf71|?0QNo@wN<DLq8mQ6cL(r0&u==5AVBK0qa1)>h4aZKG~_%r>s=p()u7%DEL(73&99l7K6fxk6ubH;N3ds
0>Oa1#X<^t_${id%i)v_fUG0Gl|lm(l_-
{AUTiR3??rKbfl+_><wja9p#|2bCby#SBo*LyH(EvRHz69a_aUq;`cHqo7>(^|*o)Ex0m=|V79&XE5HI2FBj78kj1jbFmIo60FpR
Bu3!JuUvt<+vzI7p3*neze(v>5AmtL#LNNk9`<#l%+4{wX%1LX3DP+krT1v_*zSo+v{xc5L?{o8Gn!?C8mleRT}BMZ3WDQ$OiWH;
=2RWqzdRu{Q5HGXxjSnIeb_TBCfMfHMRqxNC%*FDRce7dR4j-
eiyO~c)^Rf+9+&u5#atyUVO%7#tcc2irqWC#bbi>lH$N03nD$k2IXcFRb(o=-NodFXuT&Ti-sgHG=~iiE7D;Qa;pa0Ke9yhhFrt>
y(z`yqdPcXu%fq1?U88h5W6=+3ZH1fyam{w8*cuK4!D013&39iS<F!9sT!Ik*wrB4S-
54p4p8cAD_$@(vbl!3kH^<;hzb147b=oA#ori$7tmBg|CxH5?_1ol&m88`!8HQDorZ%d0gd+E}lb#SH5l;VHbCXU}9M_Oi^0vtCy
X>GC~6?m7ll#mY2e`PU0!;)^WkcYv+{(`{Fi%jt>?Iht||91sT6O$oP>;<2;yJ|2RnA~fNy_efLf_IDQq4<ziqJT*4$SUp(deN2Z
Q?%>H0eEhp^F|9sF^Mj4^hZ)@P+Wd1JXU>n`b)c;Q=73`({Jy$QUGX@&(;rYybeSYrW=o#}iqD7cSokIgK9?RJm6!ZDS`nZ`f++q
@`$h>0X8i@G2z4gu?4l}WV$%m-zljd?7GG5u_^GevNj}{BeSU>Zc#u3P=lL7?9d-x&+7B}4fS|NUe=PGi>m1D-
*9!3)Fk7#M+#}?<Ye4o!2-X;JCSV3-Qqt98g6N-##2GSBC@nJ}4mwil0hK)H-yBf{-O)Avy&1^_hq>IOzY<*-o88-
t30;LFH%Fe|YQ^T9JQ-m5=!-qTHDN+|XiiZxmiO*(Yb4fg0zMJVIfv!@JT&Ja&^tzSKt<>a3A-
V9CL@?MGGH2=k6g$yxE3nwk#NMTx-~Xu>)thd)sxlwA<%v{QuqVu6QHX2iGNx4(VeAy)qsGZzB-b-
$$t3=#aB@>kR<HZ^1X&2mc|dLZ@x5|>Mg`+Cv8_Gu$Pf?L<*)7PfXY-?$+0O#3$Euh&kf0Zca@rJF|K-Yq#Ur-
{oxvkAQRg+<?=bWZT+4BssSx*oo|&O}W~zOlzHzsnjhy$Q_^`3@%rAL+-2s&@asXsqcHSelsHx&JW7E&CMfAE6DEU-
p$Lh(=DId+aOKvp~KatozgL9Fg2Mh!WByS2#Bz#F4}fIe6)lZ*q8LYhc=tB1G|G7Y247^-Uj$WFlVtsdJ>cZiL=<yJD(pjXtK-
@W`mXnOvyMZ3MH7<uvtf39%z4}g$Kokn0z%F{)0s*Ll&fB`}Fv@<19Tyg1>wD@>z1tz}!G)bkXKy^u=*JCwixAhLuqYK_it$;)-
_lsPF8?6B(6<0qSfKSv@gJ$!S~?Ra~<UwCUluNS`SKy1ecdiFgi{NV=d}pkvePO%n?J5uKTVP@X3&L#JF0Xxhcps#yaNNvfhOs6w
No3t?<)E@L3mDLCg&6Lr1Tfo|X#UVnE$%lTmHJb&@3ST4US-h@iL%$NCjovpsh=S3DNga16Os&(Z33#2^t^7Nzs4^T@31QY-
O00;m803iV11(lVt7ytmQegFU+0000_aAj^mXJu}5Ole{-Qe|^+Z*FsCL1$%dbS`jt?LBLg+s2XK_gCQHa*33<^vX%9E-
X<l`7GyDk)^~|?nP~2kR0wJ3j#DAT5Wc>>OSQMT-`6sFS+iX_h1GDcO}QU80A`lz)Vk1Prs)J{v`VDcVGR-
@yl$*ikcn2ShJ$ZHW{mC(Kj#N9Bry{8zsr6ZQ6<@NtA7OWz|G!QIt*EWMxqw@ixuXE-TLD`)9?~k+?l?wz<5on7qqMdABNyhP`j{
Y$=~K*;ch{+iWfG)B37dLC2$2p4N4gyxy_m*%{#bEvt8c3Hv5{pB1yC2(CDe<<n?WR@<~`0KEwyUSF~*TC+TR$EvFdyv+0R^0?i>
t2H19@K{ANn*xj@0=8zGDB)0&tjM#1CEK*RSeKW@sAl<Q65$MHQQcJI==drA%dx-<Uqy2w!<5ylbjL<?-
xlH*H7F}Uc|3M|Rcu<f%TX17KU)0p`?tmEqw)9gB&y;kt8&erzJ2`UGrEa63gP~5AHIDEARZD3{K26t3B+=L|Irsu{^{+*u?1xG1
wP_{G6Ix!0aXk*r=W*jVy3uy2hehtR!u#N@~mza@ZuCOT%78+WepEbjMh!VU~HPks@(3foFOT{2V$nje|~oSUnj@EP97bf!n}$vM
$?C1jNu*5hfTkF{pQ)rmwFn2a0D2y&ZDf5fTx?RSZ8o&E}=$NAv{fYz^QAR-ZaEV2x5UVnDKF@bpw4z<5Pnv@XAw=vbkt;R+a5;^
mq)7t86#2TOwohGM)+Ja|t7UTL2&0kg^R8Yfr5+z0HFsyNXfE78Z6MUz<bY<MD0$^cvB+eexMJefq#2hUGQeH%5$OSU_SM2xkI5H
S94y@&f8z3v)ejO=jjI2!@X1>7UB17!lO5!P<3NWKH&GmT*-
wgsF*}5bcFE6_DEc;U7SOHRmi!m*qPaZCPCdZAn)N#ThkaB$O6Bk9MGpcMWfl<~j9k()t3Lm3efTHRlmXGzs1ez`wnG1b^d6ci?;
Uelq%E22<K*MVjASvgOTo)xsZ+`^^T#@MfK*d3koTI!~LMEi5Kixi^44y~eqvtERqLRgAx>FS0zZZ^Wc;+9u1h=IRC+Vf=Qw_~X;
lM^C$meD=4;<kZq3QYUFGQrj$VD_+rN62+0wtYES7^sJskgBM;ct8@XqB%3K16Zl>*Wr9;1soun*>KA*5tBWRFKWnlkXT-ny8Rs<
TA&2iiBsC9IHdMC(`#dWyz&I!1QZP%q-
$bv<0(BVvqdP3yrUAn)TGAgt_SD;+#0`IHD$~LhNaRg?O%uC)Tf8l<NhKihinDt3z#vpou^(DiHxI_QGib-
>y{`|y7hU*|+qi?nqj?k~pf`dB&^V4BMV5B5=`*r_Y8C(`t?BF-0(&s>nWC4a91T@IS7v-
%G?l>ei2^rLcZMEZr%ehp6u?2(q5zEIw%Hv2b1b-
z+5zuv(+id?+s%lUBP*w0UIFeeUfXy=0|2Psj&O*v+hkg#TU_I~1Vzpf<K&$-@0-|G09-1dlSZcjzco*ChHe4;9SQu$mM~0Vs?#-
Fwr3*?VEp=7<ciTOLe-IE>-
nd(qz1yDf4Yv&(>h_`BETz0H=QwXpPOn#!Up0kV1SS#vyLYk&j~`Y+9Jewtl??g!P26NI)Jr7ufw_)XTYeMcHmw&39G6S1o`><72
`lH=`z{QkDsH~s;jPPPcPG~;reEZokpD&#-t|RmpF;JW-osup)ls+Uw<Po<TdyJz{K+y9hbP<%yCzUG6sRt8lQEismTe%gBAmv9?
rR1C5z4*l3(uoTiz9{?MM$ZUd(=Va&kJpmC*tB;1m`(CO9zKFoCIGrmG9bTNKQ^nEm1ep=ota%SJraT{X@G)+69Wv4(q<W&^hNJl
Ul1V+|~MP54r;C(FECUHs63(gPaqz`seCIZ#334s+ElTu%VR5GOW&Q?<;L8`nfuY?ogpXhjb)j?%Z&j~@C=Cn_x!v&LRSicR8v!x
^%QAJvS~)M2fYRa;d=fh9VG^XTgocqwRVg)_s=it88~PPXYHVW`g5s+T`fv|~)wD-qsre`nFi8Cn?mBu|$tR}ieHj_sX?OmQVL4;
@(M<DtM54-
gA0VD@8ep>bLZLs+>T(G=2_Pdyuh4`4kIWR%bCp$u!oZ5DvrW6cmJw@ISScU`vCiX~1b)57>B@ih7cC^=ho_StT{(0*$fkKVj~ox
FVg>NkJ=%l~}+;^lM8k}La*c0A9vV8n4ek5v$zCO$0f*0%jH)M$@yuB5N4S7~`syL2D(1@tsmGS_|Qu#l&-
#i8BzUh`_t*|BS@^R~F4z*kXikwvp81I|NgpHj?}VYF1G#Tgr&OdQsoP`mLd;T*?yu$2{S_I|=gK^UxPw-hIj_`r^ja?Vl+{{R~z
D)Joxi01R?gxgHzRYgxS#{gS44J~I@v}nW72xm`iztn=<HU7(TeFa$fy&*t><4IOA4z;oL)@_gZbY$K(qkD!h)mhINL~O@C@AIv^
UXdV-O@a@Ihq*2k8*na(j-$r`WF8%=j>RyhEu~z|5FZ*ZuOE%qFkf0C?stLl8sG*iK(<@mM?Nk-
wm)HBWAD>_>ReuqT7Ul4i#N&Z-_AHTpuax@6>bJ;h?h|9J<}7~!<orM>wEPk5O(+{C3Qnr!w-!o?n|1lpS^e)Bo2Ap-FWpN!T{Do
C<6Q<U5KoXz^FLhqtQ;X7>dep5ydMgFnAdznCF1Qgv3iuu(wgacu|WX;i$sD$>+a5Iq7e7fY9P47^0lJPMLh6(hxx~e%{7wC}-
m3aObP%|DL>f_436l+Z7uquXqiX&F~x!62p5=m`|1j5`56_p1=Ak`R2Rd%np=CYvMuK3(puYLlRbbhDL;3QjsYiDe%PIU4H8V_FM
2n=;hGLOC3zGNpXUohED6Dmob?#ABpbZNe1-V0lIw;758HFac%Yx7i-Ak_!j2d=f8XTpEFS6n!30))GW-suGd4&V~@yo$?eHIir#
(x5lxTU$zGhH%>+?5EwoCD70VM{8Xz|HjARf5e;2IKJAAe!6M1z4lY_6VA=T4#y&h3#BW8DPmg(FX+lngSh!tocUX<pnYUY%g(J)
=L=I&G1bs!r?3P|Q`4#<k3&WyfHYo><urpLUyNSij#6EiIqNJ;U0;T8s$X{>d&qO8{hyM=REBITg*4mA|qjP6ns1cp2Hu&OD5+T>
*#Zb+jBbAcYlp)!^NqtdhxODIed?#ym*TQgE%WN}MY)D6T(QMrjyh?_4d+MsF{36?f;b>YplZg)Efqw0}btFey(iRUg@Rj_<|4z5
_vICqTD=!n_P`9DH9<|d&r7NQ%2EAw<$Q?_q}RX@{h32tCnWGmb$G6*|HdDlOAIB_!7wH};H&3vPh4SEG04Y#D2DF<}N-
gLG%0jwC@R!e$B`#B{D=1#_s9*)FpC$yWMtjZP$bTV=BDsu=IZHQbD=DwVciZkbnO)Pe7uA8eJqd88K1UJi)<TiHFIh`Tx*V3elE
Gn{@G_zfk5Hwz)B$OfD$P%GuhH!^6QYLr#S<OjCIZJ3n;d}Q6$|9*?!GKF~gA~z9vSQaZK3kwR1p3Vah~&SNptV;Zx=~w$=nBZu<
$0E4l?Pwo2nNOwscy17kJ43>y<?U<(<sRJz})<vC$~FwK@vX7n@+!Xnt`xkIHo}157E`u3r;?7*{&{_PQN?!s=*s-
fR<^SHyq80l^fx`WrdFDw3z+U-hKKc`YmI-Xv?-`bp__T1@*Y5-
EU4p^tkG1n}SZ4<3{Tibpf=%txlxo)SN0he0=P2^fY?xWaQQ?7nm(($B$1=@2f<6thmcxb^6X@(T_M*FyZyuC9z;e`BZbCFi8`&j
EW`E3AR}B_bqF&l1TCjW>TpFiTF-
%WL}oLD3isa>u7mp4;o}ot5t~qq#lR%5{m;kmBi1(rhK#NqcAH~@41|Mch(a4qDs=sO$A6S!Oc#r*@L)(%m|ieh5Rye8xq^1HE?T
lz=H-qJ-zhpKcaK&dp_8G0+Zde^?-&!j_tIhEU$}Hx2g_3C(xQHuUsQNeqMoh(boADrIA2-
&^_Yg8j2VA2&5EjURIy8+T!C?&eDRYu5_&+s>7ZTL7{Ya*i-
{>_%qGGpZT{mZ`pHlsA3Hn^gbr@vkFy#3DCeME28Td8DXlq13Vu72&S0WkM%En8Q<<hMz`0+fOWK@B5<-
zpdPlsdGA<lpomTR_8=B<Pw~$$fi&mr{bFV^`#P(4c}hDTe7_WEspqC>3Y|VTdJWbon$wjnhxP?7PuC&~o~`%}wCj>u&GK@E8-
(`Wyj72^TS<4Tx2ZQ%2?hle5HvQuRHPUdxDtT^MKg+k{>WR2eV}3{m~SveKhVOEd4CH<x*!1I=g-
Bhzn$a6+N2(mL(tJjIQZzgyV`~FVzr6Cbj0OaNW!huDiBUy3$DKnZ?KV?h_3ZY_Oul<f#&jV`gn6&hdXe-
!rDX<AkJkVIS(Ef0!MW}xBK?$@Dlos*wg2h2m>m922wOC_mmZza-
_rK$kjie)&?apxg>SX#8e!%t3NcW`{VNj6+8XyIie?eL?G{1gBW2b2Xs0f>`lw-fYiiB^VDp4#_h04&DfW<uu-L0IQJ-Ou9<z#Sv
}pAyOH8hUfg0?NmTFrY|~UYdF0edGv(B#`UhEv0no7Et?NsQ*Tz8wy+TD(l{&x|2NskgHreOyksWo4$Sg<fOR;-
bpO=?~jBO*G1SKB_CJSoY^0!hvnw3ygr)!KX0~EzIrN?}ALo$lu^OAl($7RYxciZmw#$p_bo15kf5=sp?X`DP=vGXzqbm#qJ87<u
bHA&|B*1@T{%Go^LRoOPJuAIy}mQ>GGnjla_OxbRmY~XWLY$eIiM>wmyi@td4AO*fFViV6e*WLQC5^TI!*b6eT(LFsi7<>($Y-
eS<{4JPSb1}MSnt#m*(;HPTI&oVdphPubke<RxpE&aQ$xWj^bnR@ncr$Y)pw^4%r--xtAcGb0+B<2h2D~B}B%`U%5^Un*=sIiI_B
Q6lSa6GhiUiwP+H0FrKqWEYh!`0>cDaaGCd2D~K|;qcRz?R8&2U5wuDmstfJ{NVQv`y4d&zH8dmp1XTHL=I1Wv#zt=0ygxY~a&TN
wt1pZjUb3X7w#8mvs$Kq)aP&)&u)5=}_Whc+a(Y`bJUDa6Yrr~+3cin5vjgVCS{1*UTJA=?%1W30ho<9`L$iI&cn%qI#%L`p|sC4
b7DKk+zFFXbhBnOdY+z})5T_84uac<v@~yqz(p)2Ts4DuC)vF4z^$5H(7mH-^C{ry*CuX-
&&4;96^J?o$H)R*7(;Jb7u)g8TV+Z&?mU5lnKzvw}$t+6p&DO>&N>LWk8;!psSvIgF-kA&`~bhrzwqPAR7jr<Ivq<y*fJ&d}{rZf
Gpq=p6W*L=cXy#qBP=!u6aPnj76ES_QbV76H3qnUl1cUOjC4G*rUGPYIez#?UY@+v=>Ij|3u9AoWOC-wCEoCgX{8Al6uMTiH1$jT
4gZZYY^d>P1Huf)7T9PVL_b8Fk*DslB=bC?s91jw!nf2}u2VCal>kun%Xae0@q?y&SaJe!%v+H`CmW7CHwqgTVr=M`Gso%-
mte6jE!kQ1!y-
jGEl>CnQ(R{2P`rrvSY6?MKE2k)Vn3%V}qj4B8pLoOULW(2WUZ)nXnIVm1u@W6Vk5pONLlSY+uryJ&IH%%nE2vr~0d*2XIQHYU<7
!ZX0wFT8}N{DKu=t3(5B@|(N3hW!au5Yqt_cc<7J*I1U^W*u(GJ89q?Biy>glutLW<Ac*pI)b&H=jnF2PVsi;XIyx5Dpa3d>`8Ru
1W({F9RKRXP8y@PAv_I2IOI*(Ba$;=I1;igIB(!AUWG#DZiTF4TXDT@7=eI!2gnH1UISJIbJEmYB})ErVT1x)BZegn+Z)0<s2d&7
ClCg10<mdFaomm_eRaS%hQTog;|6SE1j2?)nZuQrp7VOvPC}0e*}Op+3i49>6s=w}-kyNg3)Q)+Xz_~o>osb&M<-
L8ff|*=+p8<_y0z(Gss(eBKBYk9Ksm#fJ<7pPHvcw;sUl`RVqXkV4tV(#1YV>hl!`#$JqdVgY_2F=H9=&fR?B8UVoiZoQo!TE1VU
}Ume9zQMWP#fl4^K`6KlF_Pf86hBds<x&*;IpFY$&KCEt|j^q-
R>bxj_|U5RYN*iUCeHHl6K)7u*Ir$h3fgW?b!w5u%WSSbFUbQa^(R>-
Q0X$&To37R;T^|TW)ARu4KnZx}3#b!9!o?5eirF{`28S_KSsw;BH*3r8xjZE%}%EG8ImBA6>X{BobkLpTUzK-fZj6COg(IWAlM#+
wOFZUq52_0{wfuB}DhzntRv=-FIl&OIeWBP&}yQyh_#@xSj0xH~c>3n&IhUVe-
(0Hb1melA>jwKf+P_rJ1@3C~tne5#iv$wsoW0u&xLB1$~;H~)l)UIOhva+pZ!mlzvt|xPSqW&0jakT-=NcEYu$-
A;{cvW7(F4dQ<HoS5Z##ekgHOS50(E)2UO*c!1D`w@2%ygCtArwHFSDagvFj-
X(X&%#5PY?gxiR#*OOjD%BWPJlM!H@cF6Pq>)<xZPB@7mTv<?9Tt`9T0)K_aFE+Fzd0`LV`#KS&_C$pY1%BD5)Jo%P2e0{P83KGg
sh>@T%Bm{0l^zI!6*9uw$Cejws|z9=xDQmdOFCLJ}=mGf@>y{OJ_DpXhY#BmFq`gNxpDq=T_q2|Ue#vby7>e_p&<mbJ?k*WCSmKE
?J-
CKa=3lB*P%dZZkja(BRf7x<#XoZc;VDN1xWfj#yGeLW`w0iyAwGDrOBXsZsuffYE5a>MbITGTPRe4Ut`_ec&Vtt$?Aosmrnek|Y&
@m40@e`V~I)b7_s!M^xusG=a30}PiC_|X<d)F&YcpV_79=i6NKA|2S8Srf7>J!gmSJBhWx3BH@A_tYp9SW3a*^xE>xk7mjmO1Zv=
RGWIr0>IQJyfqAzyvbE9^}>`m9L_f%_wD4F=Fg;kSCxFMEUnS#q_NLY6lA<AZTmu=VP#c45Plw@W>9b0qAHdoaCrjk>w|LI4Zu_T
}OY|K~TxQESnePfPBZWmcQnhM}PhA|HW_v+;lvOJe7|BXAyU{$5R9R^Y>^Y8as-
l@8*hL{JZ8jAD%XcSh%W1VFMO8oCDD}jIFUA&wz^{u$N%rW9|Z=#|a_#vIK|qJjHV~KmdrWW!z(Y&G)jbF37Vr0v~~a{*;)N&c~?
7S23c()85lwP8e<Pd|De-6irE7R5UeKr|mp3w|{5X3&&TgZxMMUh!x^Qy!iK+*3PF4MaRzfM`S$bWS&A_-
??v*sxb;@$W3f~tmx^rK;He9;gIhw&_deVfBc-
j&RxwSNl0FTQ(i=J?=KcI?uY9X(%hL6?uR37s*B0Hhw<+|N%dLF@NAC)P_0qBLvWR(Hcka6(=FGj;=6Hj|I|^;9=Dr5MIqogz5;r
A;)8siom6KFHL&rCc{N#k(zWG%)a2Ws{d^+U)e==-
VwhmXV>i`pF_%P^4}Tc04E|n8rT1Y__T{p@_y_Wcmip_<B>tVI3il__4p6b)tQj^WeIC-Ge-
9ZnF$wYIH@HJ50r@<uF(ZnE9`QH)t2AS76}>dIra0(REsi{+H{z;9iEH><ErDDCy+TDK;}4H23RCFk{NaEjNkeqBT2p?UNUy8@ew
0{29HWm__htHQIrht0m*Cyp;@(+-
1K$yLHLr;XD#UgK$IY+mKi1Ulm4@6Wyj^nOIUyQJudPwAW&0gY`Ibkb1JWFfOoL7c0sF8eU5=&xIbr*O6Sj9tz#h!3Yg}TjhxnlL
Pp6-6_yKZcRPo8<;J5t(^9?3Q_hm%sJx@yTV0eGd?dQC+0QPg<xqJPC<eh&43FQ63pBnNI-{<GNbo9~k(w$WE-
u$%ZIL4u$S{#rm^&fZirbqVvZ)^PDaWb<V{_{n6?Jpppb4KO^H`#Fb`6vB<xGc`@{jo^AK2YM~BV;U`R7HnYPG+GmrEpliLO7MMC
yfvaT<(}Y=;jUX6z_h3So<T4>&DprjfSB-ZP1#CcCX;>V}&eyh70R3lJBdCfe>a$>@px|*_YD%$wx9>mp*X(Fhubm!{h&lboC{<!
@T{I@cIMn($}_cPFAx$vfUYekO1N}M9lx+L<{$D>+j;v?_XofwI8_F_fxt<)>}IMLmB$MaX>c!NRkw2kf{In@q@ts)&0Tb==A9S0
8mQ<1QY-O00;m803iUw=!QKn0RR950ssIo0000_aAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1y@0WMwa5baY{3XkT(=b9HQVE^v8WP{C@$Fbuu>D@1p23u$`~WH8tcg?1ezhwWrMTWJl6T`XrMjQ#r@yIZ^Y
BtN~U_oO?hUmjnVTcgktE;kx&Fs(sf!fw;B*1H~rXooO(6aq|taz22x)&&`iv&1sTozTid6bl+DU@wAmoscK<BdHVIM3k}mt!|!n
qS^1aP~CLq4B|^l)k&g?E2ohc3AVDwipvnBItq_8bm7uDN~=5c70<;5)lO0M$u*MVCGdwNToYOi;fT=5fD|A`MjuNJlhwL49YP+y
;$H<@FvcW}R)NO$Vw6*+Ws7UzDP9Q_e8yr<Pr}P{!s3>*S#G>LJ^shY4PK$Zk2tb=b{3;CEbk{)nFt=^{Vm9|G$A{$#FRJQ;b0<b
Oy{2e1}U!oMRF|udfa{%>>E%^0|XQR000O8001EX8IKJrL;(N*Gy(tsG5`PoPjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVd~Z)9aJ
V`y)0b7fy<X>4U~VQpnDaCu#kF>k^!5QTUDiW40SQh+^Dy0jgTpj0A5J6YG{0+teAWSgS2>VL28K%vd#eD~hHJNpiHFORSDwXVoG
ny+dyUN@R-4x3de8p|Ch)g1lNl2V|%o~;KohCO=C#)(nGJsI2wvvPy;)G5#0D(v;evP-xOREXW%u6)|4a=TqaaZ{NJ2w!qmEjm}o
iffWt!Uj7E;K1xiHM*q;&b0%Yx+Po4@o=U!SFZSyHMvUWARm%->CkAeKM4>nU7%qLVR*9WsfHN3kQqp{dl#Kiv+U6yB7En1h>-
iZKeoSJ<aZ`!LI`w&si3CjJl42Xx}5B~V07f*yd4>OZ=JGuN-
W&UWHJ_F+<)fyXe(0m5n2|{Y$yc7{64DkB(N0T%K)BG`!RW;;#SJiUI*2Xo@e?yNOsN7QeyTu<MwAJegIHQ0|XQR000O8001EXDT
#UsO#uJ^I|2XzFaQ7mPjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVd~Z)9aJXJu|>a$$63UuJ1+WiD`eT~WbK!!QiJ=PRsn$R>5$eN
s7r(4>tabq6>_CULunHmQ<~Q6c`FBpqy!lk;r9=V#wQ^>p_<-)Kq3(|oPS1YK)#E7-
30tai2oA?jl|IuZhO*IO3=jj;iPw#Kuu#`a{eiOs?fK2RruwXMKj|Fl#Y-
ba+N>ZRJ>Z^eGM+dz4hnKFnkcghyMFS)dec#&a)9hE#vki$Tt*6mN`fJU|CN<Ic>R9WfEPp-
&Iz5@PmZUlrtA7Po8A(2Eg3f_o%&;e@ez>`thG)oKt<sn83UI0he_{5XOSoRnW34FC`NMPoX)`YkK{#CFUV+{RZBq*xS^Nr^6j*5
%VM7IJT+=xX@=Y_*l#^Q1&lQEH${$t)Aog_i;k+OWWhN3XcZ&TGO7dVP%Gk_<I*0S<KB;UeOqhr;OuQdG~q`2r8S+V%5as8RGZ%|
7E1QY-O00;m803iToQS}=-0RR9U0ssIv0000_aAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1y@0WMwaBWo~71VRU6*ZDVy}Uu|z>b!=rWaCu#k%WA_g5JmU;iXmMn0Vf||a2I`00!dS_3++lM(l`~^Qjp{Z
Q~K}K!)elLrMYuw&Wv;e^~=NCa-
#%lhs(7@?NzJLmattnq_w68#@fLT78wK8AC2|EwKkr6WwayNV~(i#Arvz=I*&c`#&nDy)w!fjauZZS>i4>N+_Gl3+dy@dnG*;nRf
>)~S5aXk(jv*4_gK+@K+8R{UJQHI8##1m!w1*0LtD{&nN(?ntG=j2Cuj-uX{rw^!1n(24sr`<Rfj8D0Oj`JqA}uPyf<=;@#ISbeH
Uaw2;pwj0wlH*I**@Tp}1@k8<pU^%^LUKI%fGPX<_}@EGHu9zvj$f1v2~$EvsjvF@Rxt8(n2GSPUPdfuFeYnY?0gL}u}zf@@6wF#
jE-xbTZaEdDaCg9Z5kP)h>@6aWAK2mk;8Apm*;h;knR006-
O001li002*LWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FGFu+WiN7NVPs!qZ)0;VaCu#jPiw<448`yM6rwx0g|@o~GT6UEpk2$7!FDo
=t*nOFF1E8$#=iR;r(<J2iJ#uHo^%EE{^51C(UNSSRi(&A-D&a#Y^#QK-Wd?08{*(e2+-!}d<3-
CMU2|nz$T45lEwFA7U3Ks84;c91s?T}rOvoXl(G7)ZXUOy+3hw^{^`saq?ett#}G;`og%)>*rK75dqO3Yli@-
SXjM<X<Wq5>qoDlcih|??@aJTLb{GZf+LLjSV0-^^2e<ob)D9*E&+DxD*ODz5V;Ig>f}-v+VTzVFT>hpUGZhe`pBTpIgYbCDEUh-
1O^w#6^M4lH;3WzANMDvu&Qcl-tD8|(WPzu2bPISw9jD1_(NUBKVdT)}Bg_}<8&FFF1QY-
O00;m803iV9hO>Gm0RRB*0RR9i0000_aAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1y@0ZggdMbT4CUWnpqIaCu#j!A`?45Jd0(id8wdmC}Adq#z;SP^qOz$pKE5aW<``#IC&CmI(3hI8LB|PuANR
&#Z5te13RYZmdB^xLnuh*fthJ4%>Aln&3N7syXo~pi*GFqYn()InSD{cO*uQKcdt7Xjaq{W2e~rR_UYtwv-
81kqS}1meu1{RlD5=ieHntfOwMAw3?`p#yiG$mRXuO-C<-
c>M)Umc6E!PkmF^dwKr6J$QsGW9OV6A06rjS!}g4@i)HVIvOq`_w}2^UB|kH<5JG6`oq-ygDPe4u7R;_ChdwzFhmmRKKq}}<VsW$
CY#hA#y8q9}pMpV!=lEpt<Q>LfSl$k*JP88EKX;%n+VYsZQd3P8aBriqPrp3>>5^S5WGOWJ6SELsP)h>@6aWAK2mk;8Apit-kl#N
6000>R001oj002*LWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FGFu`bY*ySFJx(RV_|Y+E^v8WQNd2bFbuutE39$ICUxUpR3s!gOxhS
ydw^49Qg=k8NtL9G3i0oxX<<N4)_c!+&-
MkB54Vr&oswict+zFqpc+LkhyAu<jk7HX(e$BrBm}6ovn~J{V*>_djc1d_c4Y7vn}r{IpjHHHwZKk&x0DI4BFb3#R91I;Q5_CDD1
I?Z2Jxj%snPp_OKSqX2c9LyU`qwBm6z!18GAufYjOpjiW#k~^u-
6S$xEICztIXkG}giV;ihxFp$*S~qdWRh6JkN(61Bd9SE6p@o^3shobAS0QNttxt$g608Cx;N&<{pJP0bu-
8Y1l?JI^yl&%p;bVHkq*!r>`laS4mXM2wFAF>iY(NzhyTvbeW~qA{$mM^&B#j^cR?;0aZjoHt?~R5&`uux>~PS^i|n&JnU?n*Fg^
u`f_d0|XQR000O8001EX18wd4AprmY?g0P*GXMYpPjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVd~Z*FvDcyupqWn^h#Ut@1>bY*yS
E^v8WP(e<^Fc7@^6{~V^D<$O~DV*R?silbI04HmSH^ow7M_!i_A^wi*w3OnLH8VRiyEjlh-
M{2((~xD#SDI`vts!5)W>t&UyB?Hk_hIizDKP!ud;ql81q{Yn7L&#eWN{aV6^|UKSHZbX;b6`qRf6k?3Q@gQ^}|Nh+wB_4Kg?V}d
}*@jkhzqNvw=Q?%o1a<r&9K$4XSJA9j)%jmvZ`?Q0*EnzoaH^WC8M-P=lwTGo&H8-
1fvAYs1NHDZewZ5JDi2wgFA;$$4s)7R)Xsk9`W@;3o`2@T@!@5*9a`%_ic_>G40tZtojX^bsw~M`tMpLw<Ku6-nSJ-rNEn(1a;@d
0tw1+L<UE)0OAHU9wAsEQMxQF$?hnP)h>@6aWAK2mk;8ApjCY^#@%600374001ih002*LWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8F
GFu`bY*ySFK}{oZe=cTd0kOWOT;h`z2{d9dWb?-@0ALI9t3rT-GiP&Y-e|aO;RSaY7zgtleB*J((vBAc`q-
Au)4o|SlqZ4L&C*%hk@P3A=Pkuy;d8F9*o)Sc~58zI6p*UupvaY>|#i2nu!AjyA`oXV`B7%W9*F`+?Qlk;I*JitsYnFt6Q^PE^na
u#T+S+uPEEzrqt**2F5qmRbhhl*yw@w0cT`qL)RlUdOFN#7u(dl>kd<^YtZ*u08Tbhustj#>P3zU^Y$8cE^(x>D&A@O8IQhTqGsp
Ow9$J}2^|S+-=F9Tw54sz9xMmsQ-ROm8F9$mQ|!jf#UVE(&eIU|;-)_;b*z-
KX$&oNxS6jqRZyC&e%i<vuOTr_m}RD9$i5a#Dm*xti0t?uOL0#v8hnwJ&0P#A#;`cgQ*{|2l*bKVU#;WG`NYi47{aZDrLjEc(RY^
WCqh+Bt3Ni!>Jv~)0|XQR000O8001EXOG!w>H30ws2Lb>9FaQ7mPjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVd~Z*FvDcyupvWoKn
>WpZJ3WiD`eT~Wbq!Y~ZI=PN9B2uOtwsMMXt0SU&W_OP8I)4C9;O{&BNs%ihekan;wC+qpy?>*-
U^0$}w<yMzuJS{gB8P>HXm%?sSh}zi}l&X8~9VrF6?W|)!V=N<UYrGgawj+bbFs%IGnOeoxHVQlaGm=NR2&fSGM_#OVs@U(hkp1e
+1%wwT%LcvAWN8i4m1Pn;23yLcqo6|$nI`yzrfSG#ax5mavZc>HWktS}DaiG;Yfu~D6EfUagan{H;2Cv;hlb#+F;FNld>7IY9C~J
JR`M$m3n2vh!IV%@J*keCWAfzT{$?}<&u+w!*?Hyg60s0@HX9oUTMhp)Z+lmgqH|c8y;?&-
7?#gBRvHP8!e<!33u+#fS8BSG3c++B4)Of+yO-o)A&H{NADM;t22e`_1QY-
O00;m803iTQXT9_?0RR990ssIm0000_aAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1y@0ZggdMbT4vcZDnm@WpXZXd0mmgPQx$|MDPBJRXMno(tbdsaDqdnmLie^oUE<0X)HB%Wp7&|#J}S>fdW2R
vooG&`wq(Ihu7uCXtIHp>zXW^#*oipyRJmzT?a}vXFhvU3QTu$o&l|OjBK0@V)VEZSv<tB3VmSe6gziRcrxFSGRaj`g(%<3>T#>8
-EITLugP3MTq&uK7(yYnvrO+Svox{TQ6W8b)a}VnVvDvuk}u@Anbg|pP<+Umf|fbRmnj1Xk(|I-
;FbV2n+t(%kzuM@$qeM))%_5QA?N!Pk)N4Z2q7@^RzpqAR6H`Lt7kX-fi#D}e$<fJ2j%gaw0P&)Y#a<l|Fz)GUX!9rJhFIlmSQn1
?*~_&44&d|Simb99-
CKcqF0^{CK~(n{_`J}?1qq~((F&oLVN*GO9KQH000080000X0C#((#3BIz0Pz6;05bpp08embZb4^dZgfm(VlPv9b97~GP;7N)X>
M~bLvL<$Wq5Qia%FIAd0%61ZggdMbS`jtT~I+z!!QuM`xUEla4RK!K%{VjL#37?k^`J96K`5ei5+>jlnC*6T&JZJpRAeLoteFZ>i
OX{U)u&9VZJix*tQl!0h?7V+TeRosy*-
_pi*G_!3PHIoM+9}I}($|59stR4l5dou~+PUr}SViBUOUyhze1?RrTXW)!XeF%0J9pKzwPk=`>L(8}ArDS!RiGy2nxm9J*26GJEY
zhoO|y=ZqTPQ28YdQX>nHFQ^Ti=OCr#J;G_7MFTw&#Rg0Hor#4ILeuCPFxZ}#PvKI>?3(iwsQ}_IVVXIR3i_C^SZ+3(h<9(s{}}m
0Xi(utTv<MOhtU}F`;)3jf`IYt4)jr5o}8DL-YVeEM&XzaJ^#&;T_a@4G`q1`h#yc(0|XQR000O8001EXog{{TvjG4A4FdoGF#rG
nPjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVd~Z*FvDcyupxZ*Od0Z*_EVb#yLpd0kRXi`y^|z57=T?j?a__wJxVp*<|@Hl@j-
r4%u1jbni<8EL$!+3bI>J{-ud4z@J&-
n^$7eS*V}ufMjBx+NQE`=H3O?lk!Zo*s@>=iLBOb`wvYqy#;T&NHC3j*+#qp(+?RlEqUb%P<F~L9%m3;;65bLk=Hfw5krj565p$^
0?nWg1E`7Du^pHTZ18px^<T6AJ?0lu{e;ZbKXrnPS<#kRvGf5E}JEaMq{8LR@W+bo>0kmbhxdS^Yyy0m1~1|&D*qUMWL-
5sDDNbbdxdJClqFYfG?!rd4_###Fx|vIQL`$3yeLs1ZNEC2nPL$pmQFyHQEwf4KB{JV8nzZI3oA=oi=o@)h<$*0t@yN?O<?<L>~=
Z7`3^eF%h5#%{y>i7l?1`Jv%k0dTvZ}L$g>e7l5P!(NGdfZH7Em?&-
$=QtfS1t*ffSFxwUsbxZrp@bVj2`p@h`14_62C$Qf@{QQLre0TB2BL507IcrijM(af+xXHI9=_QsE1-
gdq=Y(o9z*BsZvA<{3TvYGm$N9#<Nk_(<gR5*PUGnv9lSMc0WY*PxP)h>@6aWAK2mk;8AppQ&$W%`O001ij001%o002*LWo|)dWo
~p#X<{!^d2@7SZBT4=XK8M8FH>u2Y;1EuXJu}5FJWVJX?9_BWiD`eU6D;o12GVW@A(yj9-^?d_reN-
9tzb8?Lkjr%+9u<*`#J>l|}sTX0!DJa|+MAGw*zy!{+h!X|{5f0@G~SP!QKTN(;DOZdIFN2gbC$^ofiC*BxULz!0LKxENSXns}su
yPRxzV4==PjNahUeWz>+-
e#)Q=6SQdyEohQdIj~L$c2LZN~ZP5Tx&i!?^#zR5U`_KqZRjtLMOP#(0EF<o<1kqM9cMuZiua3fWA59%zeZLWKZxyEYP9Yy$d^Vf
d##%28toHF%^~VQ_3@eARn%D1sc<i$AYgtrC~lcG}4#Y3?q%laV6-
Xg!N~oE|pTqL$J_Ld+K$XvMj6m9eAv@0G2c{6iI9nz899abaplcMz8;jW1lP;ddns2hZrau!|ZxgEs7vfzFz=*M<<i>m6=v+675{
p4dq}LKdn^19aP2hQhfnXO9KQH000080000X0CB5qO*;Vq01*NJ05bpp08embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bQ)_8#Y;!?
pWo~pYWq5FJa&%v9WG--dT~SR>0x=N1_g75xP)HWMldLB>kbsyh2R$|8b`~4DE$I}I82`I%cNJq#oj32zn~z&)o*tfOYtxcrnyoa
sXgWh-0h`rMbiwzaRCkJ}KuUq>k3K{|=X}IyykjwN{E-~)lUVVEBlRkJZxtTRkEAK^E}=p+FU@YbQM>JS4fUVQL_m5)*;-_-
B_E8nEUS`m*i$X(BiB>C9?>^++ES?H@EK9<TdqH)CT`^d<g$qF0-;XLgK-?uTGCJq02z7=2kp;pE-
R22_MBzeF~_f7Uvlh^d1kbutfapxF%?1}Ut9~Cy0M{Qma>xSI#yOJfMXaij4`kZcrIAl#m&u-
$cFzh_NUO2qW4s?e)Nu#G0g5WYf%V+(v=+G8BH9V=W1A>3bZ$gcPVF?{I*hEJE)51RD1(aO9KQH000080000X0Kcf($}|B001E;D
05bpp08embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bQ)_8#Y;!?pWo~pYX>D+Ca&%v9WG--dT~W(U!!QuM`zu!E;8se@JyJNqp;Akc
k^`J96K{gm#IC$9RfPC={0J?=Cu??gW_I@u>X*mY^-i~F2-
jPM#_LX_D`CHFSm*2rLUd<;b|?hs@noF`X^i#KYio#Qjy<7~eP|Xmk;hSZYX>1u`nRP{a1&6*>bJUi+Kc9J*g^HDvSbim>TCx|RB
<}$VIW?lf{`OuJnM;3&FF_TYCu=<{FzZ@TdKaeLTY&ld^_icBnT<;DBV%ni-
C8mrVTHEOV?9mN27bMeN+P;%MrcuTWfrnlz$g&#Tb(`nHCgwbCf(qT1IgjC~B5K-
epXB??^a#Nm$szVv!5c?LS8L>{=A~86>M`YcLqY`XRE)L~t1HV?bV{_StzO^6G@cUI*Tk4zj#PDQ*dh<hf!$P)h>@6aWAK2mk;8A
pj)Bb?iI=000>R001!n002*LWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FH>u2Y;1EuXJu}5FKKRbbYX04E^v8WQOi!lFc7@^D^}&;R
!aK;k-`ZMm0F6F9N=V`WRqGrcI0)bBE-MrN1zCwyfZsH`?!Pp`Qc@IP%Rq5?Y=|fRj<&MaNIYncXk9J`is9f6av&ZS?56-W4-
js8e%!ePH5y1#DZq>I0|pA7IIQQk~+anKpCrF>*nz&n$zh3)gNZfAiSh(wIr%Iy(_JW7l|-
(#EL6JUTVEyXK6Z(uHyN#pq*{0`s5u_%S+(<ECC6r9;A-_8KJeNS3?-BTNsCvCFQM~cf0^D-
9WKGbdK?x?dBNUDb6nSqDu5v!8VLBNwaC8!+vQk&y-
eE+{TNF63DxZN$(vAC$9+$J6WwV5e@%iWG}8ofghn{^<)hOW7yuutTH7y4A(LsuTuH!yc2nm!r`Do-ki>}{%xhWbx<VF4f_UAO9K
QH000080000X06$I4=^X(80MY>f04@Lk08embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bQ)_8#Y;!?pWo~pYY-
w|JE^v8Wkikj=F%X9Dd5WPP(!#b6u&{!lheB(G-GiP&+|1TsHYu5@Wf9-
qG^tk1Dg5)#{NKzCv`_cX%Z=^P6E4>VJ=?)ztYN$E#1O*>N)1OoMpO#ycnFa}dmmV{4W2~tgadlLPtA%ZVjLBR;FLbtpO!YuT~dW
;U)t_rtGeB81I?exTtIrcvv-
=Pk@RkzBU$Bw*CRI4S>lWEroC|(8(BUV)r6j!Pic^PS%cgpKUhz!okIh=1bTM{g))03zbdg1LTH+N4+e+J*aDMxs;*pTh8l=t(KK
@;74<1=X_?uq6kdaw{%aJDu}6g;X=L*lJf>h+-kx1`HbhKk_MlJNa!FpPLa8F|(;jikcb)&DR9Av3XD-
AyP)h>@6aWAK2mk;8ApoltECV$G00095001rk002*LWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FH>u2Y;1EuXJu}5FLGsJWG--dT~S
R>!!QiJ=T}5<$R>6B0hNk`1cyl*L$n7tMW%5_M4D7_##ABxJNXz4kyHHq?DuS6^Y-
!Xd9~F&TEf*vp$&S_=xe^)bZqc$<WdgDaP%l8*W=`T;9#u_5VW(z3dc=o;Sh@@%@lBy!8s#g(my3_hP#L|*1oje{Z4lK{gyX>G7H
Az%ay$WqDIiWHikr%6Bb5nghx<k;0>%Y=o?W!XH>bKnopsSdQo%n6#3CG*OmepgNpB?*W2Wk=k{w+aRL57iJdf3{OZ)4VmGBJ!4z
t?AigTLWQ+mLw&x0mvyb9FFQK{&k}7IW!50id@FYE)G8U)5x+;kz_#Y#8^gT-ah%K83XE6%%)lFj6ncy+r#d0`-
4n=t_%gUt3gO0p8A7b%qrMft%vgVR~15ir?1QY-O00;m803iURzMg|E0RRB-0RR9q0000_aAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1zeCX>4qBL1$%dbT4vcaBp91X>)WgaCu!(L2kk@5WM>pD|#?Ufd@oNPwfE-
N~Pq`o~$L=fK|tiyap6i{d<i~OI4q&nc1Bg`vL0Lr?=%sw`7@?>yB*Dy(VA6cHM~Hy8)EyPvPWADbT~{d;ql81q|9*7Fpv)vUrHY
iYE><sNkGYIO?B~I>Ajug{a@_=6S1{-
EITbA7(Bfo;2ASWUeHCXk%CwiLf|OB|VK!8O`B_9?^D&d?oYchIX#y>Qi>att>%qq8{=xz%y!tdqbctgd;)gY_AWoV3#FuwO}2bp
H}j#5DOs$@?=}+sK5E;sHt&rPkl{T0tcTl48gPVcu82SI-
6x;@4D$f#_r@>Qgn_hs~2Y}8pHDOsw$JfQ~U%ActIVq^GfAP%F`hh^iz8E`EQiso}fsc3-
Jw5O9KQH000080000X07q`;(MbUS04M?g04@Lk08embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bQ)_8#Y;!?pWo~pYb76L6E^v8Wk-
=)iFc3uV`idnzC;=zA8(b)~hd|O4oI`sOTYH^~*iz6cNlod$SCXBkR3|Z-
*?E%gpnQ3Jov(F8hH1X4$#~spaye{PJJC4Xfl|%MpByO#x;t9u0gbU9y|#wM;IT(CxDR2)J$veux3*Py)YnLv<XupODBsH6(?;#K
+cgw_PNo9FO3A84=0fs8x2?>QZm^@E;F(6@15MqME99^l)!J5Ee94-
)k~zpS_yaF&1K>jhgftTp^}DTm@bu{yG6RWj&oL5<mR|cf5@hs5b%=H74z<0QWo3;I)8zNiimgT_E~Z!HSte#e2;|;WP*XF~4p&S
smECR|8*^aq#$nz&Rt_&o3r{qe3<r_rzsC0DDpGU~Ba3HiC=|o|KDzQ`a1=hz0A5i0p?RSaWT>FM4!%D9*7O%8yAfomb0&TOP)h>
@6aWAK2mk;8ApqNe-
x)*!000;Q001@s002*LWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FH>u2Y;1EuXJu}5FLPmbWnX4;Z*5;;X)bViT~Wbm!!QiJ`zu6ua
0_X7FJv&-4uy6tB!}%}v_#2F6T4VWOBnn2*-p2P`DEVH)6<jgpg26eF1NZO!?fJgWV~)Pxi#!IrD&Y(L8)f&gCnIt_b2N-
pfT2?*VeF@YV3&&wn40TWKX^F)^-
X{`bSbExD2Qe#amH6?^L<pZz2D~%msv(lvRh!x#XknI+j@?4E7WtJd=u^3iXxvKvQ?*ayfmjXl*ObKV?l^$u-
CWIo9l9U}}aAj>cX(s#^l&kO%f5z+(&m$#W$$kmy>D(rA3|wU4bqzT0|?XsUzC8Xr{hD-
#PL1oCJqsHwRQHAPCB$!_Ul!!@vX6NcV9Rt_%-3oDt;CL&t>$Jh?8B1PxWGJmm#f-
x)~V%0hoI10xyfEUz$a$c!vkIGRSR^Y~To%!!5*=>R>c`n2^P)h>@6aWAK2mk;8Aplus5CA;^000jH001ih002*LWo|)dWo~p#X<
{!^d2@7SZBT4=XK8M8FH~r0Zfj|7XD@DVbY(7Zd0mk)Ps1<}g?ImoQyJV!X}d=X6AYDFif9IyEaO~Ki^LcC97=`w@5D|E2v64c?(
W^QZ{YBF_q^O%gN|{zsn7*mTl6{XHl?UNb)Zx|gu$ayV7s1t0PP$F9V|H(Qw{a#bTc+9K6AiM1)^5z-
d<Y{36~=k;_z}P?{}))@3&C=QRV{1lR8bSnF|??*1cKR$Sg@tcUZ{L8!zCfUDcv5<aD{viVPQ@vO+d82l<4Cd<7Z|Ib#{2_tbb~U
SG#U90@gf2uFm0(XV6%Qu~JEfT*qmeuM~LsX9kUeax@hsW+)#nOF!RG@qS;3hT>yQ>^ql*>A#_B?k_EVmbuR%Ii~N<Fm|WlMwy>G
p4~CRQNuQEFQ?=Xbj8SSe2&&kK>0q&?jxf<h)YXuqrN`{%8JUnkAcs_y$l*0|XQR000O8001EXfuX;4A^`vZ(g6SfCIA2cPjF>!L
1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVeGZ)9&TVPs@3aCu#jK~KXl42AFc71lUple%%QR3xNvn6y!(_5i2IG;WDllPU2S72>~>rh}p7l
ze{nd+`laPwVI9)-
+@TEjOAho7RxeVYjJ8>s=2@wMRaBQVL9eaGn9Jb&PDB4Pw%`16k~1vkF6C>J>Y;S9mbLEmgvGq(W3LRsFD2by;qq_*a<=h$nS6dk
mqF?6i|v!WMffBx-
$rzoFH8@`ao(XR2KjiZ7`tG%^QyuQedl<+=nDO;$1kiM|VCjp>tb8N<8$&cs3pfnl%>Xll>1r#R_X*(KSSBZt6#V#w@+@_0%terG
nD3a?HN*DScBZ%ENc99cX%OVJpXccUs#0#9+#7Vw0IC+C$Kcc46VCaQ+C*ZE(N?Bbs#$A$O-
P)h>@6aWAK2mk;8AppNJ^aB?G006@Q001Ze002*LWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FH~=2Z!cqPWnpqIaCu#j!A`?442JJ{
3JVU|q;3yTsazO`NgG9K4{(Y?;%<@JWQske3i0lw>0pSQqR;;Q|MopJFPqoZ&KdNCtF1-Pu5%bm*l%0W#V~+U-
I>o3l>#@MLS)e12iEL@Co%Vg6MB6}Vnrh{4vItQl|H#2Nt1D#s1VIt(?0E0Th}|N{!|tM(#uNIYobbWut63Xdp%$!O^-
TW$x(aTW31%-
xl$VpRiDx#8CimSoCLr}gtp$)&^zL_{3^s!2%%~81}t{hQL}$uqqs$xj7uPnGt<nGRMeNuQvSQUx$qwB_@7ZYM}rDK(#YyLcudBy
dYHP(+z>Hc)`Pxi$FuWVO-rkYhZHrA`H+j>AjQqU$c{_#4Nyx11QY-O00;m803iU<s|?dB0RRBw0RR9f0000_aAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1zhHWN$BHY;SXAE^v8WkU>wwFbsw7`4!eUWRtq>Ua6eMVbVsC+5?;-
)3_s|O{O?ws}TR4G#w0)Q}p@S@7Z@yJ#C(sJJXP5T5dJjU|K^yhyAt|t#>^r)t<u1lTu*%qw@jKS{E=FXIV@dcO;94*sOTqK)nji
bqbH>r=?1`j#P;1rK%tHsxHeN6n`pn0r92IrbFgJ2B)3O61Lb=A)C%IUCA3--H|Wk^tn>)8ZJJiCT?U7a*zHU5bAPMf{8wW3~7j7
$qXd=1CKJJ*T!nPtOH$w{K~{a2!TA<1~j!-
t0`YvGrL6{gXO@%PYgrwtUR6*i~G%HQ{mO=;Xh+{@(n5ah$D+fXDJ%P@_tn1N#H47-U6P{gvoiO#-
k`t2NP98I`sTENOtqjlH)>r15ir?1QY-O00;m803iUBU=OSr0RRBU0RR9i0000_aAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1zhHWN$BHY;SXAVQg$JaCu#j!A`?442JJ{3Tqs)N!=cxQn@e=lQxRf9^e#(#2t~^c#1Qo3i0lw>0pSQqR;>D
-}W6e&)b*v-Wl|a>zzd(UFR^AaM-n?3p9XI-
8r5EDg|yhQHY?ur>LVN&tlfl3B5ihv*M8>4k{A$N}t@1rOCKWREXxaX&(=&t?NBhe=17>>1C(sHFG5+S&~J@UJqDF(-Wia`zw6c-
u4(OIe)IylHux8T4W<jkPnjwk_p;+TZ2n!ypdmpSP3CCkKTaA?%HdfA+J*0#+kxP;2376V+^c<zGRkmSS;qk8`<$cV>$<e3O`cI>
WMt2U|8Qzsxk`#rt5mp7wzJlyiwEQD&Wy2)tHaD{2ipY<rg_|CB6YrO9KQH000080000X0Iy#~WEueg0L%dZ04e|g08embZb4^dZ
gfm(VlPv9b97~GP;7N)X>M~bRBvQ&FJpCba%FCGE^v8WkilxhFbsz8ehSeY+(Oz12xO=3P-
vGya@bDBbCkxASVeYL!q~gdb+UELC-X_a{$F~4>Sh1BJz9g#<Mz;?3%0e$Ih+o)Xqg63svX0~s1(@YLL5LlM?nWm&WpK+F6i_*ij
|*yz(EC~Ug?YdkyHuSkqS}0RrS+J)n$2v;!kBQAiktDz4pG4ff|xo!cGrZNHa1=mxXoOH9c}6=g&eLGQRkf4SFMUkX1)l2pz(rg}
U6A&|4pN@+%V?A%ymmGtgkWOq_$HeX@I|TY?;X;F;+V*ell8#Nr~W)m(U|X8O-
OjciciM;uu^lf!5X+s9j1o*EeAi5=*xwqbVOsoVC7@f@S_lrFmd4U*mcv*frD-%v{f1QY-
O00;m803iSl^8pDY0RRBp0RR9g0000_aAj^mXJu}5Ole{-Q+acAWo=Mwb!TaAb1zhHWN$BIWo%`1WiD`eU63(v!Y~kpcmIkL9Sl-
{JyJTsfCNpYWN0Vr8egcT#76c}h^qegIu0#WJz3wq=l6UMP(5#6mV48X4Yb^8vTRyIK8M4u7Oi(ZDAk_%>`5sw{mFR-wAL}QaW;r
a<4$Dp7|kjSfvH#QT&M74ek@hOb)-
U6uT{N0sJbloQ2d$91;mq_O@|>AlAU%kOW0yhh1Ap$(+$0&)gAdlPL~_it_j6wRE9?8AUDYY2z9wB!NjPQ%s`?)hH-
54+E`83HPe;lS0)xh2n>U5KvR2*n2M$UW%rI_qZ|VJi6OHO%Ht)m__5h+8oW6@{Aa<PeM5>q;*-
UbvlN42`8cZbB=8hhZUHZ7cuHQWaU06h(L~jdHa!0=lHK#Ol(-
PzP)h>@6aWAK2mk;8Apmp1SP3Zs007?s001Wd002*LWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FH~=2Z!cwJX>=}dd0mh(Z^AGTg?I
mo6CDgvfIU(=!GHu!rDSL)%Z)G860wo*Qi!Vl_c{(ORWn)Ny~}&=9-
w;Oye#*&K}WdU8FXx0iy?=@t`=?Z9VpfI+y_(&Y<Kp7K|AMJv-OU|r158T`WTlL4aC?f_Wq>w+5W6l3D=PdQN336_Mqyr+(YqaG8
YiPwAq|AQ6bqIFSCT5?y!((EZ@MpcIJekkkjKvjc=&<lm@AhImm6)gNC}?lwhOHN@gH+IMO(@W^J9p>zeV(Yl@9}l3$rv2q82Lt^
tGX&1cG%DrWbXW2hX6!^AXmAQki_vDj@kn+9**4F4JVJ~XKCBmS~@@(!ahEFVWzo&*8o)g9=I9y^TAD>WWO1w7iQ8q$&Hzd^FQf0
i5<;u}y)0|XQR000O8001EXTFF9nAprmY-
T?prF8}}lPjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVeHbZKm9ba^jfXJu}5Uu<t@E^v8WP)lmVFc97A6hpdD0!|KKa97PDkWay0v
@4<7<5*xzMl-H!O7C7pcAHYI#GCh<d4T-
+>1BH~C0fGmp+d{1Ht1709STu<*MU;?z=KDnz;wOy4BA@9nvJt0W{&I8>T3`ynuxJe>|CpKZ+;|sgo}U*k-z4}{-
lb_<p|lI$yz{oQCYT{D3b%5*6<{gII+6JOwKW_yDn&>ZPlXB<osFC%9WIT$_lBJDaidt-)duFY|tZcgAi>X*nlCR#*KC-
zY?(#LTH+72^H3h_uMNAl6%Eln-qxsjA>?1%Ih&=VXxI{9=y3~`j3$te2EI*gJpJh7DF&>A8)KQ5<G^BThOC6JSXqeat!71Y65YJ
H(vjCN$wSr7`hSPP)h>@6aWAK2mk;8Apm33Q1vDO007?s001xm002*LWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FI9ADY-
x0PFJ*FaZ*pH|X>4UKaCu#j!D_=W42JK13eg?hLed8aWH49{g?1ezhwWs%L}?9)9VBO67<>0QPPUHuWPbh9|4DaHJU_mq2UDSCO!
qZfZyJM?!Es-ThFk|qHG>}rl>*cCjyz~<o!8zt%VPGp9<4ryX2m0W?38z|Rk}AnEk%^epbAmE7Uk}!%G2op`Jc*KKzOmUYBh5%2X
9*AN14Qm)g9&%i5#iMw7AF@ZR-{(m-A;)YgcjpDQo0PW*~PTeXEUyi@U-
pz&=c{KsdoM#F@O6Uy0ZVAvBM+f*PA;_6!#HOKyx4P6q60*0lG;iu5&VVX@U}F1)#V{I9Vas6vJBVPyW~EQVl6?<ZFl4TRz37W7p
cKPPY1at%dzHo-
W?Bd>p1k{d!2LpS0ZP)h>@6aWAK2mk;8Apn$D%fUMV000L9001xm002*LWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FI9ADY-
x0PFKlUZbYFCDZ)|feaCu!(%WA_g5WMRvmiC|ooP2=6J++5G(iH4NdlDOa?FeMaXypV``tOzHv?=vT%<S$w{0QaS^ZRD6YqCt6T|
+kLR+G=+u&YGtT@OmNV;DUt1-c)c4}jLXfI&OUVwrIRS?uDn;)w(GDmZ5p4*F-MOmG!ZA<B=kdO4`-c-
%wrhgk`TU)rn<G8b|T+UPLJEHM^)Dx}dI(s{nYXS9tWU&!TgLmO9f@hKbPTIL}4aSPBGzzb@FCqqy>PccdZgBd$*lQ6?+f*J#L&Q
EaF;S7A9{m*y29#ZD5{K~{y2!TA=I#TV;!xA9%klnM)wsYX%7Ysx2tUO*577KWIScsErrvDhb(buHt5>FPd&QcVH&C@)UrvXp#*I
2+S>aZwp)vYz<sf(%ol-gSTddcn<vLw0|-%v{f1QY-O00;m803iTxeOZwy0RRB&0RR9p0000_aAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1zkNX>4h9c`tBmVPj=zZ){{`a&s<ld0kLJYQr!Pyz3Q9dQbvR9$;{x&>jLwQ?L*1No=HbB9J8`$qA<P?^R^C
Db-
2L%<jz21JrNN@9UkGWCN|Yifq)aCSSsS+pyNV4uoijICv5Qbk{o{0j+frqjom1N#lC5cuK<}j3H7dqH{)IuYX4B3^xg7tp2E*m%V
5XhaFUZm?eYs@}x8vLdA!ujgBKPGGno$iuVR3ot;tS!%UpfDnq{F(`QDNlcD<Lih|@N@cQhofEUyTkA~oo5<lG%Lvl|$Bf;Oz8~#
<W6=Mv;XeB6WXO}5tzO}gLy+tb_L_c8|qYuL4HDl?>#bP3kPL2Pu;07;A&?T*`UY(_64C}|6s>}jUseTK1MI9&SjhLGeo=!Rm$6W
aGH%oDkP-
N2;`vy=;0|XQR000O8001EX5N3wFUjYCBR0041F#rGnPjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVeHbZKm9ba^juY;|X8ZeL_?V{
<NWd0kOKPQx$|y!#caa&Rl9<z6YA;83ZhNXY?CmT@+zrNoZxO{)kY@d#eXOR$|35I$M6Gdr`pH&8s?Kd<*%q4BuhRcJ`p8r>ESyO
Pz;b|6GO(BM!A&|PmGfi%XFByEjn6UX*wWD~@~kDjm-WNj;Cudk9K!DT=hD_)B7;ULQ6aS!>Q%925NNvT@tea;8ct)`J@sbXY@Iq
%z{(MD8O`58Y+Q?=-
FK7D3167n}*p;vqhi{fN2AQkDeB&=ZS5=lcBVy9ukTos^Hr@6{~3gb7647hZS4}E6)+n5EGo?I4Yk7C)b;Opb_+L$b8<9k%ZgZR}
}V-#PhS61x8-
!ryij7dKl1r^rwJkvJPQnTO1M8y`O?^GsoUO0J4SlH%bF%_cYf6Uv#DHM1PE%QffFc`!7F0!_X;4s`dtl=UxP0kxJpFlWlbRdrDv
df<=*>8j_nXcG3P)h>@6aWAK2mk;8Apm2Zql+j3008R&001=r002*LWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FI9ADY-
x0PFLGgSWN&R>bY*RDY+-a|E^v8WP{B^aFbuutD=au<le%%QR8DZ1v@t|`fKwD2cZ+C~%5j-
0#J`iJ9YgqJz4z?*>{}?GA6{2mTcZoO+8A_f8;g{~Zc~Ydd<RN30}q5sf$e%v4B9!*nyq(1Od8*#(}y^$!WbAk#oo6{_x3VUCb){
I5anB0J?>Ps-*2J#!z={EN|SY~Ln!3HwzWLUEHO@ZSV+>&_-KG#-
)hF0J4UocD&*A6sPT0uzNEoW%N*njI)em!M5qU%7&rFTeOPz6o7Tc*?OJ|kVkv~sVRSVZY-WooWV$uG<~>KtAuvstW~QJ>pAr_2y
t$c(cW=i3SnvbYsPHqcES|i>Xbh|Svno#l!uWm%`lKyS&TBP)MiCxt6prcPi{C8SHA0q5m*NLdO9KQH000080000X02K6Rcq#z^0
PFz(05Jdn08embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bRdi`=X>@rnbZ={AZeMkCVP|D7aCu#j!D_=W5Jd0#iX}ZL0Vf||a8K<ak
TeDR(4K^9trHPjYov98DgE~<vfGsUB;L+=X7>Tg*QdAj&erGxuD1pq+s2~LVZW_J<EaCsnt=z8N`dWq@(kKJV$GIZ5R-
;_bov<0DvW`#Q%uw<-
P<2anQ#@U5aoMWJ?~X@IP9SKGg%6VUvk#14xx|(+t%_ZvovwK!$LBh(WxQCxS5}{GcEc;PLG)yszdQ94Tf6gAj=b7A$cKrA@$}HL
X2YQJzcCp4<17w_ri_*%EU?tp~L8EFxbpFQ_Hk$b}xMEmP24aG0p6Q^7@)s+;Xv)1|MX`|18kpYgBlNzbszJVGM@#<4u((fya1%2
l}clPstlKpGJ8++9({;#h1TbvU`Org|5UmP)h>@6aWAK2mk;8Apj;93R6`9001}w001ul002*LWo|)dWo~p#X<{!^d2@7SZBT4=X
K8M8FI9ADY-
x0PFLZBjY+q<)Y;Z1cd0kOKPQx$|y!#caa&Rl9<sK=V;83ZhNXY?CmT@+zCC83zhY}DHkKl#81ltL;!Y6BHc4v0?3d)Du$MsGM)D
G9%8nu^=M4Q8YTam_^4j5|&KUic8WY-((fop9%_tI!bCXMM)^EMPSH#(0U^TsH~d-+>ZCb$YHA>~t9-R)U*IP9RfV3q{JOO--
#=L$M_siYrimKe=DENJ47sQMW_a$PI51)V-
KS{vbtcUq$pGzVH9%?Y%z9ar)V>qrk>h?|Ch##k^KK^TkIy&77nQ;ZGGfO6Zq*dhY3bl$Gu`|}I%l?$I#DOXfJn|h2&)5oq{U9cY
+SrJ0G8?}HMn>qC~aavq<9zIs&5S%8Adv6`H{FJb;vBhE{qTheanZXKV_!3$c_hG1D4C|Yy%9FrixTOYu;?hsf8#b?*S!`txj_G>
Kzbx4~LY7Qd<Ofho0|XQR000O8001EXX__o)qyPW_CIJ8dCIA2cPjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVeRUukY>bYEXCaCvQ
x!3x4K5Jd0!icl{KtsfwG^HNYKwt^tC#CBU2(nPYU(7!jd1hKleoj0?yD_ItYYj&g>4P%x!XgsxqZYNK9C0b{D3D6FHa0no&e_H3
IGRAu4$r={3XZui$5wC>|Q;zJhudLPSVn1U??A<u)7e-
g;p(FFHH^jAlp#z?R;6svAu@M45X&t`V%iH8kKBtp(sl=m^{MJSCw=lrFcmq&N0|XQR000O8001EXF4PALD+>Ss4krKrA^-
pYPjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVeUVRL0JaCyaAZI9c=5&o`Uv0*=$G;|F5Re*{ZiHjPr8zXluS{w{|k6KBLDU#h?-
dVZafA7rfJ1NN*r$G;}C6P0;^YYB>%#wd%*YAJ$*VWsm7M&7TZ#JUS&9)J8#ooQSS!`v0U{$pp^(aMEvF0%JQZwFlz2>^<JGC%08
?JfXa;1cFME=r}fxvdNWKs+*uZ7_lxZbzTouhsaKg|t&9D<N{{bp>%4P5d!n{MaszUq!k_C0S~e%FeHy=Xo_bUEs#^;bJJh+4a!>
Ij-&AC(q|o4#-V#=A``BwI73CHvLOye-ReiOYOgEEeB+i*nHA7tyV6<S2>-
U1CAlYQf+y%d%@Nn;IM;R4to9_mXYlU*8FKH#V)lYC87gAi7sOa5~e#SuTk6CsFr@gXlJ51FmZYvK_cyt;}uwBWHN#w_vPU|9v~|
z*Og;pj2SJ{`d9G>vz@7k3YTzdjm!8Dew=~smQW*hB{=+<aWmoVx5UiqbE1^#*^#Je3{(c^tD<)X6TV@#j@AH&p0#kS;pl~;bnvd
{=VxsNBmv)odzqjry#5d_HcFVYH;$_uAOsq$&zucrK%)<STYo}WG`QSdcY-
$RiYDw*a*AXi#S$|V)wjlAm|VV4v^7Y>TxI;h7~YqEme$50nk=`dk=&y|D|b<3m+p5LKQg61hVhoQ!2njqrl2~zhtVn!9tlxEyb<
@6du7@kOz=x?5^oHBvIT8xNa9_0t}Vyv2<`VR)oN<5X=h~t?<k8uh=R4ySOb}xK^NRt#5&Oi4r~l4W)Aq9_M4Lt1Yj=UB@+&6~qQ
!<4_1z4BQ1dM6BRtWX%o5hIgQQKLX7iEDtyS%3CGqUegVuu2j7j2OckuS@?{_`%(Wcem*o6xLHAQBbT91{%qW#`cc-RLU^vIU_qt
$JErqQ>KZRD86@!l*jSTkRQ;s+ZWcOFX{&r}zFL^^DB!=UhF<Ba=^9;Cxf1QRU{`-3sR8o+-
Oo@5%c@dBV~PM}k`BlQxffsrnTXd)_$7E(HGYer70N)EaurdoURc{MhhF%?LP+8$i|5FUBAF3(jhyH*gEWWWM$(!sOWlF_*C;5dn
s>D@5-=^6EI`JqB8l9ugmmRj=-
d>%f|kpQ5(t_hj~tX1B*_~k*gttYiq}&1GT&y8ByT&mE#c*9MX6b$Sgcc0{AX;W*kp+zQ?+g0lPe}m8jtV8E*R0z)V1Q#)Pye;`D
{zvs;BL^9Ae80;Y~CN?4os=+8sS{#g`mEGw723hY{-
foq+x9AoRZ9P}RkdyQQ;4+(iV>Gcvi7*$O+^U8&s8l}0=ggGXN3_79L&#oRtnmq?)s8xYu)W|ZJoFZUd-
$;{cF{hh+ru{KT$wQH92_ZSDNjJAOcrIN}Te1`B5w`t!D<3y*K#W8@tn0{fSWRF3Wr!$b10=nhSh_)sVvLA%hM{lkNP$<)hJywRp
Td1o~<)g2LPuV%~+)7tL{A4c<OA#Ho?lwjChtO-D1I21u5)2iU%+AQ2*95u@MHqV5jfLgZYJ+1UjCQw&M(-
=L1>5wW?Z?a6rb?zyTk~isJCe)=uA}dX*md+h($2Mtt^`$5Y=soA_@3B^!C%iRN~CDaMZ}SM2t(=|AWn2I($L-
eiX8?z+0bk5DX!K*)*TV#%>@8aW!J{ux2icbVO1|H?0xg8YRj1+L0;I2cBUrghH=T#oeWKz=d|<cA5rBWV+FpER0HBgr$yca#7+n
f9|0BfS@SC~lK95or;8WR8Qh1{JC4RDAcPhY#DM)I{v5#{h6rooB{+byXS4WEc9`-
rxw}AB?QTTI4UXhjG@mJAq!~(;exx$Jb<|cv|K0a`Is*_G=Xp*lB0Z4M2P}+?c|~5Rs-
m>mfNctU{7$F5q)j}@1oLp9d3*|5wmshjWS!(#oe&OEU?8n~Xp1Z3f{L!^UiVob0`t5Eo~wB1a@xsEu<@(kQjE(RSX$-9Y-
90UZgZj262Hqmqw}0mkV4s;j+72VH+UcZfAkAtilg3iC8`M7Okmpg5c$Ql^KPTH4t#ia;A{wxD$HQ<R*A#GDQW2>pGZ_NYOc<c8l
3&kKpNk!jpF1WRJ54Wl+X#=@i(80aVGHL(rhd-
a{c+jEKKtSJTaa*X*r7Qq)>yuZ`LeD!gE%jHmB;hPJho_Ov*S$;npvPUMFGmt_2Bwx%&syZFBH9D|goiND{_3e9*9Y={?u%lMsVq
Bk+7X5R-|Y%>X*pg-Ajn0^nY(freX6&sfftKuZob*>BIw0EFKqpxQI32|BH14wQDql176WE+=sI18LZ948J?z08Js1k59#En9neS
o95XWISM=uFP>{Qx_q$Xjoa;J<JJTmiE}5z0D$v0b*!nQ{sx@^=t%f)cB<*~$ALD4lQStg?|CCBQl1ZotKATjyqF8HlPbx$G^qZc
v=3nVB#!EYh~KQg#Q~WBHG(#Tle_!HCg#E(1V!O3G#WT%vh=Zo6!i#Y`Cha~n%DYK1M=mj?(tcM#gFl=uPlD+T}MZ6^A3)*EnJTu
oo(Uu<q3v@i57YQyuAnx!k?yVUHg?wPxIwg%SHrs@S;lb8RR4x;3nD7AR!W{-
!m;U<WMiQ*yKTq+_n8(p1mxGV^$Q&5a1b0(~)=VF>}=z$?;(cOyv0WiNy;MeMyfl6b2;4a#n>lW_lvnce?4u(9mmhPG4b*N%%26y
kBV<{E=1-r}3qh4Lur>J*T1DW<QKW+tiStaocX6bv&9TZQhfqTeq{~uf;r8lrLwkbmt5qbxxiz#N$&Kf#|$v;;{Hxz~yNv8I-
&f!*3sBoS2uhS_<qy(UvS8m?eLxY)mb8UL^CTy=v2FCO3MF=;gZXh_ll!6Q@!HHLHQ6qU&^Kdr|})xd&!^9_!jkN0gifWIJf<h74
gvw73z+&nVn9fj3jg;g#E%6cK|L%b_1~D>q%siu|9iHGQ07T^2pKefbip3+p@;HD0F<dOUQV%#pSDY#tRykA?BjI>06`?CMdXl<{
d?1nKl}%;eHZ^q)y2e+ViCA=B5fFe1YpXj1P{H!7atmeG<*!J1`dR{q>KT@LhC+i|;XKIgcB4p<Kpqqf=kr|Bh?1F<O|@nY%D3}0
NmSh5$@ivrJK6H_l|uRqgHTtViC*By)(NX7=6v7@plCFY4z;^%qR8NOvCZ@xDf8soA-
)UZhU=0u5CjVYvR+t)N4Tr5P`te~*?ND_XR<Ulz;jWhs#Lkl~EeowELu<)jaukE<libV*{CgpQtK^zWLBgg*?OC>sm@3c_b;XG+*
ZBrGw`!+Hc6Vv=O-GUpmoDZ#;&<}v;tU&W&lk;;e2F+g62R>j9+);cn>k}WRr<~-
n7`j#?3&C@CrBfMnU#}tW6+W(leg5dY4UGc8i}r1V(uTJf#W))%2+F=P@y5To@bTmM{Q3A1z}B$=re50N_kum_dkC0kAz=frKk=P
u0)*1v9-zO0@fAkk`$qQN0q9i8ZX6K&OD=j3uxgv#UOx!@pS^nj#()vhL2yWehdmwc0VG-
&eBFx{%DkQvJ=~#EJ9(c1eQ5XbtOtGR?UJ~UMlWY645!)ZWcVDJw6JbdJ(;dvYPdTQI7O_xJAteDT1NJ+lNW>tKfFe4s*23a&%Y`
{c)IfqPm&52MC&j~Z|8^drmaZMj4hr~YHnrFE=s!4&T8M{Dpj-VIKGo+>8PTE#ac*}q*{*dqQbI_w!wKZG_Rlh7f?$B1QY-
O00;m803iSeV{b*j1^@uu82|tq0000_aAj^mXJu}5Ole{-RBvQ&Q)O~?X=7zBaCzNWUvJws5P$clAhZWdo1>-
=eKG0)UYlV7nl+eRY=CPBibOkXWl9t2Bwm{DzB`h#L{hf1VSAZhEFF*c_s8R%z9X}n_rITgU>W6to?YdXOSWRP9+T^<`CwI-
8<Hfet=!f$NeJ6iWi3g{c_~xLN-hQiL;E61-
aOyQP0>83V#hO9Hm@}uXsL2nF}`jjPWf&yNai2ke@tfc>HO0ynSQvM&Ms$ULY@W$enDAL9*oWZNYm0xvU}=MWto>QjnfC01dlnGf
aK=UtQ4uFbr1a^WwM8Sn`U2&vQJP}l!E5CV4k{kpPZMxhnkg}s-Uu0j#=_oR*W-o=j?fg7{9;#Y5M8I+=}(}^rnq-CoFLsH}ab3U
tC=H&Yhi|De1{?KVQu+XE)P#m&vb}AhM=0n#c+o*1>1-Ll6xHS&<4sK7zdI8qhX}WX))O4+tD<xj}FPXd`GKsnS}2F|Sr-y-
B4+#6YB3HX=-vn5LX4G+n>@^dqUa0NxFaLBc?Z%IONw3z3jX5(-+ZB64;?et{@!Rro`4oCtvPRwSFWO6v4sOoXh-
H^m8F;NM~XEY0rdnB**z3)nWoy-R2F-Wv3WCQQ<eKt;-
^5ph&1D+?y%!WO!0t%e<mq>mC5z)A?Oq^u!yQ4FuF3Zp$ITM;;{`wguKC5FPm=47$lQ)RugS(L>&=)nUX7iF4@uo2d3p^q7@B)L?
7P!~?AF;+21E`*Y2G}L-V%J1mZc0*CQ$O@Wr9a1ACa^sElNEvM6tpb68Q;~-
MR^NSEY%y)PCEju>vb3Th##n`02icEuv&}vMvDn^*0SQKW-QQ;XP^*jaoAdK!YdS~B7wk`Jz-
DaMF9)pGi(p4+o@`J+`W|TQ>+dVP@tR5_Wz-ghPH4Mv*QTlGaW8TK*@_Hxe)$4;E7>$ZAZyZv0#pX2m@sY(u(0C;4VgyjxH>RXic
2UVd`qo`=Aa?kJU{_5P@)P~fF#H^guFpYpE3S9JgC|PB2FvJK<I6H@+kPzc8rxG4XaT<pUy9ED&Ks>S<V^eE*g}V`?tu~@@!E&;2
HN?P_=dSNNKe3@PeY)EjumKq__4%bCY-B(qHd;0c4!Ql>^&aOMs;MpNVEabS*~~&I<-
t3gEo)Ar@7^BvM5fdAJWIfyO>p8()aHuXH!smowa_m4qN|L|#WOZ*wj@?7*5^cI?fK4)yO<M&ko&z=S9!-
vblH1+Xm}QAclf>`6@UPTc5CW{e6Cy7uB8z`9XMsv^zkU0LMd_sQa@P~I`1r~U9teN)){l4lGIR0BmfmD~l+1%XPM#C1-
bZH4D?@R<kkmy&V246TBvc9W_UXwzb-i9_&i2z}%*dL~bL0fRqWJ_oiGw~X&sJHeG{4f3I(%jsii<*%(g$Kt$af>yE?ZqL>(-
<J7KC7~sK-`QLMo)hHJ9Tl*b1%z{6Z>i=|*^*mm%@>SIlS#K)8D}&o?T{+-bkSA52KKptP<1)-
Q|m{U`F3*)!_F}lZRv3(5Otp+XmjlMJ}Q95dwf38z;?og1!2D%Ul5s1sk0Zpd35`%SV?GD4y*1xXgaxS>Le;%uhjj*1Tg%uWi`x5
U5Tx<n2DUNp|-lUJAVXg06AgH3y>nO-RgKw-cA(vTT)Q2&YkFKYK)!0IO?Xvb79r-
fs|Y5cJaF8YnX1HT1%cSZ`{LRN#~U21(vXm&u$BfKXv%gx~2k9KqakVygTR<rbbIQ1!JL`o@JxJ-
*O}reVIg4F#D@=%OQi!;F?&I>ot31d_T8#N7fPP%&dsTiUM6o3QYyMqXoV?lPc;>gr0@larN+|j6cH;F@^x+fi%}mU`b1wb_VWnb
)6g;#LSjauVN>xt@b`<C(HVt?KMkXMvCN*c$(ZsNq68%%)c;4cLqs2{!#4C>Uav>Z2j%|^0dNMm>#hmjqSkok~s=Hnfwqqv}=l|4
;LLwXgNoRbJY)_#K^kKjRm&2&Isns^b0crtM7)|Z~W-
cwOGiqPS^DK7ai9_JvBPP{3kQ^u?+T1Q26I1(HV12O*Lkq(Vsg?zG7>0F?VFqP5FfhYxsPT$#(zOwbZn-
8s|<w+Y^@m*31KabvMspq$)t<;YXzR)IB^$8}gTbp=i2j*WB*M5q*W7hG#PjH;gHMZf?Gx$D*LL3eQiE&|38Ws#QJ)jDAP=?%AIt
lruI7jdPf6qbJUL%M3_M5?D<VEH0Wn?7IkuX3wyvd1%*qKEkz&2fh!q4AzH7ATI}h0Z>Z=1QY-
O00;m803iU@#~n%zF#rJj%K!iz0000_aAj^mXJu}5Ole{-RBvx=L}_zyVRU0?E^v9>eO-
?nNpjdbe?__0#`NqqYi5?qU2ZR%>p7CUM~UPR<WP6Q%(%9uyLzT>s;l~{syQ6@HgGTu!+=kad|t>hq{GRE<+Fu*u%!pzlOOa`_y>
GHLGh89m0#7}!{yyA)Bri%RgsaAk&%&+k&%(_1uvdG_~FgR*(fdQ^yZ^+S~S@tORGWf<k8`cNmWjRIG)U#d6mX-kWFW0)dWdVlug
oPWl`T?nC5Dh6=(AOesR?g?k9PkoaX5b@$kHv=JI<|UlpUQls}tns=%_Mo~5Hk{Zv5XY%<BSQ~9$>x#n5YoWo;T^)vV>K}KcKq^}
#T(2we}5EMsGk|H@vtLR|=MOxR;7KuVV5P;9}`B_$oKi^C0R04kg;NTDArw8%#hc8|}KI{hvv$WVh0}e81KR7JQ{QG5jai0kh_+D
JqO*&<mTH@;62;jr7uvnjdzpT@W0iUO5S>04u{TtgiZp4QN2an?~pC7z@7VkfPwEyDai(nWms7QF3p2l^WRHO57K)*u971n7nj;G
KxXg0o*U&ZTjmgMDGjc@p?d~psHm(`W02v;L<)+WRf=zQ?-i+x}X)BECZ|M2CD_~Da-KX|0k+ni^`1qct8e)IEhB<?1yrdg5X`1m
)!`18M!&#^)D=%;@sA5F46<!Artf5>Ok(Okg&^6%8Mw(Y<9#m|0aHk_aS=YJ!gj?R;YpZ(dtfAf<+dGo8kRA|a^T9Neg`@j6J^3A
L&TU!3(e^;oW`;$>qi|48-qbgNs-u%`7R9wBt@>~G_@~>MYV}baWztRzdT#3j3PqD5Xmx3QZm(S)+mS@eCpjcrYr;}u!H`-
(9wi}~7sp}wC@{9s01@KAsIx7ZTIt;%z&+_JGRs;=zz?fv1;5;eDd0N$=DaJ5xYZ#=X^9bN?P(i3Qh_OVRG))zkReV~GuX=TwPx=
8qs^coT90Y)?AK)wT_5F+Vs;2MT!OeU4mkGfS6$7b4BvCv|sydBdPq~J=r;u)|0+X@|03RrvfY7QJ_<5D&^AxaAx#%oydH}O+fMg
SfG7I9TN<m!~{5Aq2vste#Dqi-mSpkp`hT95;fJiqoi&zq3$yQ>S;1Y4KNT#V^O()kpoVrXhrGle6Pt#d%cl+%b35-
zG1jC^e;3x;8Lz6rFMj=NC(a4_3T*0OAxCo;km08i_0t8DH#i&bTRQ^5uZ=1RkzhQqe%57vXl|%j(XLV0d7N^r042AVAsM1*(dzv
ArV@5J%Q2jI!jfqvc-
ugOV4rpMev}#}|P5eT95>k_}YaOu?RlvMVWjlq^!w=?XmHv31Rp~f1an{MJbc~c}Z51SQGYLfxQFwdMSDz>kb@hqZAyu-TRiHz&S
4opvy!!Dx1(jnkiykqzuE#>1>R8q%dKFb|k1%(T3X->IMJK`L$)D+KoaN)`I9z^5JDSFh9GH^~Oa(4OL(J`7K?1&o#(}8A2)-
UIWdnm|Uf6VqB7_*3$ZSswnE#;o5GJz8%{#!^w5rOg9)=)<c`^cy9S!zA+}+(hS>HD(Zmd6&OzR`I#ITR#GlEpVuG4ke!zOET@l@
dPF;egAYw^+6W%!YURwzwuZaYkQZrFIR60VMc>Mb@eE{gK9kdqg7LCEvfP<4kp)uDM~O?0Xnn(@>xYvwcOt#$@f&s+PUMOe<OQ5v
VOz_uCSY9;tOcv=?NoA`$T-H8+Im+zBd6Ckxj2v|7dS83H`H832_p!2j{2AD<>nLmoycRUAgD2q6%oQGtxvU~#7XxgUZXm-
^SOJ*iCXBbGMMJp{{3IxKy6M}7Oab#LFIxkCT4Aw~$nzAk*YqC2@V?~uJMuLnLO41zStpUO2Mgr!Bi42z^%&LK^ydS7W4P*sN-
*Axy*0oty8S~=c?OW_s!GglI$|L+DBgtikWpyAYf<T(@*t_BHf^XrM5*ZZ^W}w6qpkxp%B(i1DTfn!Tz_Yy!U_n;Z+iL|(F&kHaF
|5_*zXhI4hzOR{^<@S#WJp5iGJoT`CgB2o7d`m^R|V;G>B{nTyZy=im){GR53IL-zg@4B^Dg@xR8lfJhbg3{^{i2O4#d}}zd&Q5>
Jn?H(APYet8fnR@|^K>v-)WnoSBjhyiQ&v89Bm$>VT;X-
%cE%t9wj>t>P`+XA<A4ZySN7yI09sccZ^_TFfSijZB|(5em87iPcdNXbN6!BqusHn0DPN#z~U^Ghp8R-
WBlT(Sbw~k(HVDgpFyjQ5KCvUn%Wx18Ga8QJ&ElMb8_;_Z(pSaIX_%Vstyj*|?{3ix;xmgT5CH66b$2N@nP18rodd`5C%J-
S&6&4vV!pkj<V*UyssR6Fj6p=xj}De6~UW_6cV&fzd;V0eY!v0V#ej+1zYRGTp~SD>yKI*`FJu5S2wPJxzkw1JHtvumH*EYdykWT
T%*QEDHH0SP+FT)N`C3G*@&~&u5_b>bj?RVJYuXhPFG<)Dv}?{UF*zK(;<J+Y72}vD~JiKC-buOBABcPO#AnytRf{A#qj(#01;Sp
H=fBjRiM!f7S}GUzfH14t#*JGl%QPV7vZEDrh+3F%52h?k@l6aqX_?N#`c|a!`OO*SP8{Fa%_&C@(M5%JK)G?+bx&I<L~Gp5<B7t
HPuHaeeXuF1{4Wju7a$)w`uG@I)gS3QV3UE#hG`pMm;GdkeK&&__QsERf`vc$!YdbC3bt@c}WIPJy*`xNNJwfRzw1V4A${?e=L9X
uQOih+vnwxw~!jWO0Ui0^M#$(4Z5*a@0Blgy^cC?$QkUu-mrAJ5GnROic4S)#O_;N;bWdSvU*Iy`~nOJNy6+o9e#6&p6E`mPqcr9
1U(_ffJ_yQtC%zqky?8O>DtpK;&0b&cV78g?i$z3oN=JN@lPK9)nRUcru{L+O893?F&$Wmf_*2*}|+47o|{SvPI#x*()rCTA$FsB
av(>^c;C#mGfpcZ|ZN~m!~O=PP7-
i4DfK<gg`0w_TRKVqj8Ua(dBKG^Oiw&Sl$U@!62jtAR5s2fYCG$`)C`wq~ZtncS77A3hurY4p(Boow!kF4;F&yH~masf|8t;uN)W
XW`f66Y$SG4=h+hGK6Yfwqjr4LG&MsB7jsV48_mj@q0suE5j~yY<)XkbScpo#J<}vcU>$9)S`2e$1)FQW7uIA{UZjOJE8`=cE^KR
t{Kn^HK29rXk!XfZI7*693Oa%j*!@F~H|r6*Vbm=+NC=0oQ~W$_ao6){5AoyVU2m)Dzh*_?t&=t*>z=3gI|}%w14mHoQeJ6sOm-
0t5s)zmrtx%^rwuGd!r+6T7k(CqEk9A4oQ3f_&%7awh;s}#nc}u`TZiFJW()IMZJl1n^n4pj(%qmCWJkoAu&;Lbqj6S`lFHdV@@z
zUENs<4ZkySx729sIauS8`?NpR)ccC3>+Fqu~wRS>$H+IS<y3%z6*#b<Yfc&jzA&iD}dYZ20;!2MQI+qYuE+t#PlFx4^>yv^Yn*}
2EgxZT;h7zW)Nc@d`E>N+za5S$fG#+$PI@)hYG;Y&fX=+xzn5N?_Q7@KcQP{2`zjzra`$5c32+~8=hP46NF&MQb8{jnc0PpGH4pF
<R3sy*g^wIf)3Bs44*>L-)1q@E-O#@?RUceMZ@6cbV?JrenJ%i=AR=x6`v~Ce56^R-
I3q_lBrD!@+gb4kP!%ZB92{IyWdanH}Ga@f^@Ks?K5`6`NR!(D>HfMQfrwBD6BGh;*dIQ`vvBz@`HZ$<jvo`((-
On1ZS1wct%p_b~q*qJmMVic)p$uW_i*O|vaD*lzV?ZCzos=dhM=^!Jc`Ii*gZDTL>vNQ-RvIT5p9cfBzJv#t=V>9gM8Wi)*DLj+t
e<xAefwgPfQPirPbe|mq(YZtb6%D6vvZ<>wi7PWs(@87A(OFZ8&pnD&(nNn)qQO@5`JV9itXYtY|%1T`=q|IXcY2yGce5S^b!7fg
72O+Ud+-
_Hn|ECUheT`O&Xm=fx`vfqZjim`K(PU$K|Lt=5Z>CPwl7}K^`|ntO^lsg|`<pEI`ards9qgK(Qet;adwrwA_k<eQhrVS7E_os~>E
M2r&|lo<-g?LH=QYAB=}>%PH;CBeGH4rasYqMBh&~7*7<@#vTVtrgCOg2Lnysoq>GMpmpPHM82$k>(xTH*23IcLmoBUu?--jMF8_
cR;m<&+W}OSB8mv2N4>_~{A@`B>1aggXpf%IB1WzYJVo=YU|$9XrTz!IAA{4YU<69|43~%DiPJhJvTYX=;b{$4Of1&nj_A*c+ZHf
{ev~=hR{3!QlYK$SRzR{h7}>#W1}A$0lii@?6#>aEdQX6|Cpft?Fxf%q1S-
2h%H9BF7m*#XYzHfM1uE;GC23P3b`0e9Ew6`%#`GBk|L}i<MX?Ot{N$Tpp#}$HE82zs);O(4s8+VN#S~kh=#gl-
^^jn<3*zHqK~l907DS-jrsUGg?EwG~Y0J<vK$N@WxH!ya0~ix|-leDS;{UW4d5?%psx#7_^$yNJpP6N6bcTQx5CzK8Z_;g%KmM-
e8&S4>H2AbTxXv`&R8_yDX_aeS5$(Cj6zn%CRa4q&*<2Mm_O@WdCiXT;{&zmMTMQ#PJpjdGE?E(efnZTG9$WoS>yTmK?t$z5gWAC
zW%ia@eX$k@$y|?#V>5kFox!);zD8;MVXoq7Ctfe$e_qQCUvwL8h>Njn@jBL0A55jW)jI`>Zl3+?H0HPZ_8C8M#sof=aU`gIaLTg
?#x9r2X%Pw)j(?5@w?Ql5e89K|f~cj5KwpegII1Q|?8Nlypu>X)2fVQf(v*%tB?TYY)*5oWUHYw;%TZp|sT*)F`h<w-
?i3;jZLy9p7kwkP0~J0#lI%ijE+mSqu6;{}?Ssx&OsfON{Epb>^#NX&XGu<hJU-
s7YVy&^3IQS9$`!Y+9qhldTQYtvBFfFtBsR`7Sn|GRz6)*a3!=u|^zrMpjy$Tym72a1oV0+69Q{9{r@i~bv~O>YYHVW(Lo_5GS{D
4XA=2aD{dJ{Kj(m6E9|4vV6PT)b2Ld|@?+bq-
_9V=gT7_GvU$#z`??imZDQ+=*r+U5J&SCXR4(RdgccC~ZJTSP?7&|5Edbd0!?ed*sX_vUZI}Iy1%Lspq@|un_TSo~NQV2fV!^Z0(
y^J@pumEnYSw!x{^~O`Dt!CNQ+p7*S=_VUW2PiTMD)^eVdG%wGt{@1OfW_7Hi2?XcEfy#W3h?xUJ(o(8n;If7ts1?O&wjnC^@60w
-}vi~6OH0`HC)!UNKUf=5o}<OlI1&&*PFz$#*QOp3d=Pp^2Ho$+JIygb%BPRZC9IwjqPQ>Y3ETt@6I|8-
{IuI0ekO8hdHZY?wSpjz;b5=cOy3n2fg-^_r2f&OoF3EY*3u1c=#aALAi`dFg-?1eih8-fB-
|xbM}&x?<6bgY|LA7NF6H`4eg70H34pbwxUR&vLJsZkLkJ;TX}dGJ}=8zAS$bQ<Ahk+B7=5HP2@cnF5z$=78gQol)-C^-
)dsaYr)Q2B)#rQgu0_5!Lx#@{LzTaPVyG3$G9DRw0nY<qw;=6v{7t0ehgghnMiWG^;HxHB2-
lwMZMzbPF|Dn=!=8rPxcRkhtHoMJU^kd8q`NU3Vy+T0@Ya>(L!hzMAI?~LI-nr2%Vu?&*HZoT&7hTJUuuJ(%0!|j%O--MITN<>Qa
nQCy_~N82)vD!e8T|7Tmu5>Z`9*pTPIvG%rUNUSuZS(|OH%>j`iSh8%`F(N1)cU*SCWDy@P)cyaKw71lbkW?c1)5GoyH4mVWAR&0
o|#X*w;K>By)4h1r<0))G)fQyl{7i|J^ln;L6^SUQ`MhKU@>uZDSdbp&`<T={N29E7kEH!oPj8K6Mr@Clfr1dD7rR)Lf0>yak`Dw
2T|J9qHe{)>FPmz-SV6!rJcRp7Vc26tW4<>nXRu2L2k&9)L7Nb^)P;Qp{`;Q;TC{ywChY_cBu^d+*4_wac)Z<qXZyoJ<G?x?6<}@
EhNbmE3YR=cF)3!ecj(iRO;N?H>XkYL(B6(qD(ZCODMXrbP?^v>}-
a}C^)Wku)g*~;?OF+?r<MDU`w2cP_y*CVYUF$%nMtwh`5(7iMZb+8*Y||{c%FATj4`Nu(i;5!b*9R%?&%mr5;oLB$Up-Zm*V@f$O
4I-y+f!(9N77^Y;0MgpnhY!g<-vl_c(7P|mi}rGd}STfZed<FmH#xAPLDohR|4|}%IbxU1#dKTvnq@to7G~-
t^M&YtmLOV_8&hQ8$B)QpjJ}kuh>50<rB}kjZ7Ew1GTW71dN?~R8XYj+nw<J;_AdWlK-
;6gk|FZ;3)@LIT4ZVpdj$bWmYt4g@G#5v^g)wbrd{FD~zlkVTkw#axV;u*HNoG?$dd;AelhnV3JiZBcIN*eEb>UgXM8X#xw3)iyf
S_65B<=P7u!v>tUo5tdDg&CRw%|R3OwZ&!Vo1fz#uZjKXN6Hdiy4akDd6cce!Qdy^LTt-
?Vr3@rYdF$NT0AdPt5ouZ|=b2^NYm&Nkb&tfSC{<aK1aJ<Lb(8p4JE&rKE0U)JE95*e~NZ0`~NIAZ}VKh%3PI9xUiD(h-
q<TAQLq=N3_VRW}h;31(XZ9LLroUR5)Z!iIv(R4As?z&P#eQjrrrNjf8#pkW0&J)O%)4dM_|j$I$1vb({Vdi-
`8CABS~^%SI@Gm*$UYE3jYB)bo;f2>1BWJ~6%NX0LK1D3kz60PmazeV>>pAXwP_@1T`=rEtE+d%Q2)_)DaWoEs&5V+(Ivz7tJO-Q
Glu5R7PMt8ADW5Jft_~z?7Wbh;rO=hg#uPf?jk$Iuo!ie`T;uh@M-
TNK5OCV2OZ=*sm0;`Zm&>i7vciaHO8k0P=mNIo&z3jn>0Mw1T*jB8ge@DnDlsnyo+O#?gY#?RIw9r0*h9<%X`5kEJm55InPmvoaC
sWwnrw@4%j5L9%-@8=^Bn|kod5)FD>Vl@O3x^G~b6;w+Zd8;PrQ2jpr25-
nn|vhE^{+6r2rjzHJM^wBd&R(JZ66lb(r?95GvnFjm|#&5|1azREa+6ANl~%6q|H6g<e#x5UR`$dtu03WV(*7(5ds7>iTHlM$mQV
1ztqCCpj6ebMLTH=oC8O&Sq=8#AEL_v)?CA?0O(31+QyspcG^xA6XXI=WCIEK^I8Q5J!<nT#66nSgND=h-
a4bM_@HpEN{ydX|i?6if5$A`RMfsXKat)E$uy6){KN1{hr`Ucl(&Y2M_nAte?L{im)v4PM#GN$)PyrJx+i6w?d!btsQH<#d&_=em
)Y*1mUnF=Ju(;|gUrv3ckgjs;Q37r&tD9FoxfMb3upQ&{W+Kf+01p+RnsL}p`cI9U93>TV%7z~3?8I*sEMwc%t^=C4xO$lfOH)4F
_3MdlJfE4L9dt+W^Lj+Rwg0Iz0ylNZ-Mqf}tf2W9qY9nK<8G|Em)`?N716Rbt{ySAQwPz-OwgLzX<Cd1w6quUnxdVU5A#fHzXO~T
+lqN|0XMFV#s2v|lm*GqD2t%x7BM?xnW27x(cQ&K76$!;^oEm{Kf)F*0Qk|9~<5J5uJX0qYMr{1;Zu+F9BTYHY%{`Tkxvv$>h)*s
yB!KpA$u40*sm+h&prV-D3hRNYLwB>0q+Pth|sg_|TnNobSkPy3N-
l!*IVdXTFYQi2Gr>FBXzoRNV*l(wMFemRHJpJO)^CvNGb__Vk_g`S=7*+K_I(`I`J%;M|gRI>(4SrVS@^OtvY@gix7~oMJO0=igr
0)P*8xLuo%xdy2<GJ8yS^}!F$VNR_?P-
e^<tr7xyty^5!%u^kl9A}yZW$@Ki0cT9u7F1#2C@Li>C|L=NI@CfW+7`wb~dX@H({<|UOdJ_%vCwBEnk3YW#@vhyJL+};=UFgG8B
JT5ibKWL>tx$wZU_-
i}3XR!^e*wK2Tg2i9@d?ea6xSw@Xm~!N@I%Jl<0U*3Jtsk81@00z1pIQHJ}uNqu4Oh^?i4|Jk$W2Y<ARbe7qULI2wld}ELQyu6HA
`SXtRbtMQU9~#x@CS{ICQREo~Yh<d!CxM?;t`&_<esLrOn|UqpqwVxKdm--uCq<}5dom(8O|XkVfe8bq&d!PiueLBnB|D@1TXYXa
q+oic@nVWJ?)Y+`e0CPmkF<exh(*&g+>Q)>_~fzJrYu3wKLd%z!;+lLr5vX_9O$!yhlF<Mm`!k6!H@uh1J?hr5RXg&*>uCxD0Oiu
wri|?8I`$&PEVjQ!Yy-
^0b@AQpihMF&OxY%*a%?@eIiqN;4cR&rL5cpApxHFV&)Ky?nBrJol$_|dwgC9g<czwo1xbW5PF}_La|nz-
`$9{3Yu8!xHmMSg@)RcWC<<^7C&9lGKTYJ@?{nw55M2fA}f(eNjP)MCUux4+L$d*h8S9sdhM?6kC{s58ik$tnR{^azE*AVkIBu)V
>=cdOwbeKjSvwa#p6<#fU@S>B)WbxnW0^aRxGnHHB6DZS=A|DP_l-$_ekxMgIk{M?4)1fld7aEs#V-
Ru%_B1&rg%lMQ3e{#I8#Pqj*&!P9H1lbvPc<fn`1?>kDbrDI)A`|J81nq<KdLc;04X?1`NspHX*hW;+PFj|z4UJud8hEzU(%eDj2
>(KzelMw*O4SCc5AC|}wQyE?;73#=l+r9{_C*l~%EHYL|8ld$ni@1`ofirH<~aS|G9h&X36U-
Fa`tBy8DwBDh^%cDuxGL<3K?I%Gv&ZjFus}!RV5E6YXFva+e25&TY{c@mjLirv0PRy<R*h%mOgExVlZU(m^KEwnRmz{J$h91@FS&
q@hlw7u&rf%>3_nD2h1K1~#?QIjGD{WRa+ND1BEk|BYOvlv&p4@_68PqmwrBTqgfj1PWOiLVNMK;?$Wzdzor})8e^cJbTf!e-
WvpFgo-NJjQr{3JGHa2JMr@SAzY5fT6*8i<GT}3q>95=jx>`(04l9ju#c89F?`~9}u03=`6a|PgMwL1Vmlkg=U1P~5^)+*D359v%
&C@ii?cweOKQ-%DvnT7s$D|`s}S?5R4c-`$wAViz{6O6jY&;!H6%IE&*$Qfn`nm66K<uR&216<9}vyFdx>2?(J4Nb8DH%^-
*<4e;(EZdkT((Oel--kBxvWk_c`-
19C#~ZtQDe(>^T#t@DD;2SMA;QWQvIR>&>;onY00oJ{!|w$TzsO#52q~%+cJfi?^h6$=5E1&c`_>umjvqq-
$TL>y20C45nunVkX?A%IgNm$E?iyZO-L|hbk9^U}bZIpQ<Sl8^rT_zF*A&p6K<k_UzN;}ehE#~FF^!usAF#LdMOwYeMq-eMA&)Os
z&llnNz>5niV0jWdZD5Gi3x`E1b86_NH>amId3?nnQ%#1cV@;}ku`DL#>JZ3c4BT2N+0vkv;l-
xc*UwB6ym7Igt{SoElpa=C|~vxH_A^t?HaV9oa+LOaIF=E^1d3+-
n5J+mT%?x&xp={9<8_+&U2ft7qtiONFi#`+k~i`;#x=Q{8oX^{lMxgEAkn8p(PB%__Y{rPm~oJHwtLjB^-
9dL8m}?1M@{=@lAKhmLy&n&gse@OT3(rW6V25yWye@+@X|>$P-
E&4pshf1o16&VL%mga~{x=Cl0Bcl$xP?Y8dZ|9pe8hv+_w~{>xtlv4{%U-f@3y%cUcLJdxPe4Rc(T2wtrp-
T+LU*4E`DHFDm2#rL|`^dX4`J-
WoVU_3Nnnb%;bn7m8;s1+FTKNWaaO2$Zrr{}^`0p}h`mhjG)c3RqzKQJrwap4<Ynm~9I4jv<r3Gy~a#7XfC{VFemz8)e~%tH}+1n
^{FQGfyG&+w^tbWa1O)NbGW+t3lq6_<*;PCm{OXFOU_-o0r-
HO_d`w$vRI+Ob7Dj~8W|l9|Q%x=dHXqbOq0{yhk_n~TDTvGE^0F&ZL|v8#X~b3WQwDu`9ovgZo0RWw`$D`eAUX=G?rJt7{Nav&2o
3Ml+#0myWT0)lUcGeKk~M*%`VZICv(ql6MqEI^syQ9#j83#82oDS*TS8<R-IC^6wr3q+<}lsv+pEr^z4(HH*!oZmziT4-
kwtN!f}A35yoi(^}3N{qaJi3PF|yYSRloK@u+-mw**CP+p)qdUG3S(D`A`(-w6&iU@IVX(LB8*Ts`@LfcEqO2B|-
sl$<O)&v2Jdt49VcU#CSqw<38q7Tm_~ReJ`;2f$mUlQ7zWMY29RirZ_W?fmKlnf(xGCPO<ckdKASK1t2dg9N6c7>{(}jA1S@1q4(
~Eu+ubTNRPkojtU0-
O}K`1(y1(SYk2X}`peqN8!i=%;hdV=l4*c62n2@vM4mYT9WJG$ADc0yN0sNcc8VAl!76qHDG+W@q8XV*Het5qhy9^E7`$INdV+gG
sKoRCfvFgr)FxPGI<R?^N|X>-
I{Q>v}odLapMAA65_2?v^axXW{@iwtWIY3M5(1gCg{PrYFO9(E|owGgB08i87Bbo+>63xv^X8Sc=-
{F&w!eU$6NK3Ip>Phg^Z4~wp4c2Xa#oyRp3wQDUWbcqnmZASxH%zT@vy*@AL5W8tNw9_o>)OOLl4Fa#-
o~HGc&)#jZ_T9ei8(iJCk?QG!bQ?-Pa*AZyHq*8t?lQqNWnK_@7t|m(#WgE1-;4DBuQjAPgN^m7+M(#HET+sKjvsas-
lZ2mo@1zW`g#UyLX@3*cTevv47+&ibbbmiFe@?UmEPK3a{M@9zq@mK&vvN-
YMk}&Em|U$cX#L!fU8RHIUCw7yy*e8)Tqh)Z{0lH*(D8=yh^x{fAP22$j9XwX9!=}M%DkDHBo_Y*g~cM-dQupWm97_-
~9X=>Pk_8zmW?=|1LY)rl;B<Z7#<ZAdvb!+M6tE_7sb4Dre&<+>Lg%tprxU<cV>cZ8h$!%EsJxKl?Sd3a@|B6gcPB=HWn(kpsKi%
YI-
t7=55_NxqQJC<^n1U6wVbTbiC5g}ptE!e7mc0=X@fUHIm&{^bAv`cFd>3g^5Q<Tt<g>3<1VprPDn0JwFxIlIZF=>MD9co^RP@Wb8
Rk3Rn7!`mNydh5=IcW&?A4)1ZLcXuTGy{)eL*WkW=>-L9xAAbr}-
1&6xlij^L;XS0b8#5&wQ%$oQD^<i;iHzIYPJEJ7ZwofTOpyA_&sP2{tw!w)*LaH)o7Q`~yI>&OwmBHthDq-
+wyi}aVWZr}yqd7i0Py>mun8!}Y=P;k5`@DU&snKRs=CUGwnBOPkyS#Ug8|x@t+ZEmMdDpHqICb)EY)_B$^^~Nx+~cnTBM!!kVKQ
bv%r<IN5MrPRG~-2LLpx6^4OHzaNr1YcL~9}%?lW8^FCi)*|m!rgGv@O9<C~-
w{PP@ZX4Y<>neSV;;ojE<=Q8m@OlF`0C$^aJziPSbqjJhtT_(YQ{xp9wEOK*gU`IsG(AgN=tn0MTSEpcKe9{c)(e8`zq?=+ZsUOk
t?W1eRNp-?5}Eq$ff<1YZ-nla%P^Zm(y$T@nS^it^zVa(Zf@CuFkx#ySzXY+uxp_etFH(cT;@`D2@~0Zz?b%^v{0>a{fLYu@X~IC
hHQC5Zh6PPJ?|&k>#Q($yh#+H%lh(q0=_A)7)$3<pf<y;&21h4!b4T_ZhE`Zy>`nTKcbX#GCA}jkL9Lk*l}Fh*cPQC{Z(|>dE*o@
E6P}#gW7@TE@Ek|OphF2lz42h^g5gKZayiyL$*5{4OXSz9qx4-
+R_ccyG!kjEv7$#<2|vD)HzM=WD$1kW~JDqRW8BCuKLObZpz&6P78JKirLV<Of5@hUPr4p+T?mW>009gVlNT-fpp?bGnxo{Tetrv
M0Q#20=>hw7Q;U!e{e^ZuTJkUF#L-
I1a||E=<j=|boG<!k|7JE`9k(fyI*Bx?NS{y)b<Sw5ZP5j`NerXbb@AA2ErQl*3eApZFFSM{JHIE8wJIxZ@!de%16yL?SJ|3>0$h
2|A+C5!-
vmam?a!X@zByl76HnoGxXn{YQmeg(okNGtv~EpRgf(uAnCgeV3<t;P~0PHWJb5TM{|=6HRWn&bkm*NLtWA7$=X`Q!e*2q!S7g~bf
}Web;h?#5U5C7sX+|g-EJ%50d5hJ<|q(3-W4<`kz2bIP<?CHzpbzyS-TqP2X_e99c`<_vrE|KR`Kf~cdwSpYJ0QVwyd5anlCgK&a
l-)tJ{xRi@E`Xd`}qz+4-AQJ)I8l?4IMi&P?b0anV&4h%bw?dvCt^>DPC6#1C<qfbHRc1&rf=S_XI1>Ai(!O+e-
FB+&Ln<aPlNp=$d^tL<(QoLA{&cpNrogPk2h{&_YYe!RQ4d;62!Pd~c-@vTp8efr^@+k408RsEa4zq^y%`-
i^{?w;OzjxNCgdh}(D<Ro0~EHr1KBp`V6lmAAAC@LDbHQ=oPSyDcZ(+Q~VMx$Hj<z4-
I2kEzO?d|S<w0Gy@JA0q*eYE?@?b{y{>Hq83NO~aourSt-OU056`>vaBAKv<S?+(y#3;1{Y_9x7@zxZ3Da&6N`JW-t3bf-rOC&r#
=7v#yO`nhhp8d$z*W#0xNBu&piY(^*31sUYa2{>)PQQjOp_FKFykx$u#eiGOY@g7X~nJB9*f|3H?=LHxU!qw4XGORx{gTxQ**68z
<{H7YPu*;jy32P4(KkhB(Zu4b|Va;*THW#niBzw|RPUu98elm0)zdqtuoK~38cp<poSAfYB#CEhA-
9Kr$hVYrsJLkBN?2UZ85MSdo=-Q}u-
C!21+CO*v@#$=hudJ1^Zos9@ZONqd9+4H+IdyrLh0gM@#!9DJ*IVlNS!1mW5Z7YI&$~>8quRB~Lf`fbOEtFS<%8yM>YVcB*QiQqP
~rUq!3PxB{y`8fLq_O^{fT1s`dFR)1p|FLYg%WKVcn@q#7_+R>9Q<N)?{9vC~WP?1oNf6O3kXkN)Ps|23nUnF9`E8lBXQqm^|x}W
RJ7-IiKS}$6sxFOF5lmz%9mrYM^R9;=_W)802P@<nkC0&xe-
3bOKeK%dG1w8RxxPC;a1b9wb%TdMA;4gp^i7@=l#3I85{OtV*VoXX~_V>?>@-{i421E0v0Cs}969o0KLFGa`;NzG|r-
oK{&n!7tdz8Qxx$;fcO02dT*SH5VJfe9ujvvL|6`|2}0t=9^4d+u)^5c-
4i2>1EB=IEmHYIFR|n@j@NG7b>FzVswdUjvnefeFZ8e(t`wA#wRRJB5VAHG7GYDT)g*Qu#bi5z^y2+#m$Q+9{06`)za$QX1V}bA<
^MY04(f#DmrD^i^JsXv-Tcw&P_!EH3EJBkD}lU?4mhz3juW9NdB4KUpT07F{rxTy#qb+h9c>NcHZQT%O@I6!#kcRTQ3*P+lkx}*X
LnFP6KnH>IwwrAX9dnZwQk!tHswISk#tsN1;(BJn`JPLrVo!lf8z}AOQ!4w!6kzSWYG|eS5MkKH%_dyk6tQA3k~(1w6#`ORQ*Y(Y
;?{P)(sgc9TLK@dED}rMSxKiz{(`TJ60V>v1;CnnCdKZa_<3`{1u*!(93aUO^vU30LDih$9TludY;NMZif)eRMr7G4(})RH45n3I
w5dHY0SJj<fl6Q(BQs(1S3P(1fLJZxFeRF6;$Gh+JfSSfExT|Jy2N?rliqd3JW*O=6Xe&PnO(l!DF&{a$m&Q<i|&0cBi-
;dizJi$dt@5}jHDHAS3X%}VHlngT^pKNq;ohHYw_#1gWqO}93bkk_jl#V6G<_2itUp6Vu0jOTW{n+cVUb>Y4&E1<jvvhoBkPN5U*
q!5D#X*zq6rWXKsm8S%W_Mx|3kBU(~hvDC{XGd~pN8<@kUo0F-
2tV0f%Z#Nx{Be0C6ag)YSWWcR!z0oLCyvH+q5@IDEpf85WAnh?sDgv1kN=p)KlJd~Io>aKIRLJY(9(dWG$>MuIRJ5HmJPhG><Uwz
4Hv>S;^ZxuSQpjJ$~+t4wSb~wPBwxNXD#SHkX;(x{QyWw8y;%-
iXy2KGI{U`#U+wD8IUq`@cn>$$dRIca9M$s45+S{v@0;ka8!%dV)#Qj2PXAt)T<HSH8{Q~bDV*Nr9*w1qdWx3Y56L37=s2D-
f}320F$FgVN3_-pst(KG-
)X1Dniipm_TGZAJgrF_63=ANZ0N7@X<sx$Y2)oq6TKdLUZ60(Qi(4UM`Mld3hWTj?K92<FJ2BSB}9e0OCggboUA+kFI8<zAMOk6)
xSbhkE@cpKs1b^&p<`@r5DXPq(=#V9fI??sf872{-fsj4KGo-
@Ad4(4Yg}$ewN_UN<kRh{#o@M@y2kqb^|mdS14sM)!rW7R4X9F~ul83qnInu7JP4f{}(f&`}ex@f`*Ga~K`fKtLq)3zllQs5wtwf
k2N&lpeSY7U+9evliT5vUHa-Tso39;s^(s??1r24P-u|sq4TT$~W4os>R7!AM&)Jp*}8o27p091F5~~b0D+N(%?d%8s-
n273T=R#~Ee9vYI53vPSHvm6|ZAaI>ID&cJ@899uisC-sh4{`A#l2J&u=NlKY+J#D{_ccrOj(^Y7=Tm<f_c1H3FlNM|QY8qEMoYI
AFL=!jCs8vwQC$WI}ti7%V^J66Aalp4dL-
)`n0DW}_2)6*NddlxhJa$Rn&o7fJvHD=rXv)MMC{iE*IKlVB(Y8XrWgSg>eYN`Cp}ZVzXOaR&ggY~}3R*=6iO-
=@p*%_)r~|1X$*ng<wu?nB>0I)5gK_r|FP`P|2rwoNo<3}q^S9Ba@P!7RrAcAn(|d9bf#QUhn2wE}m6YEI*q4_$!2ve`z(<1f4DG
G2u#&IHj$-!*ov3dUDD%qVE3EA+X;ccK7pG`NM+G7o9QBGKrK1<VhiSiYK7R9)Z-
Nx3NV4B>#%BhjCxn>FnLGkaYR7i<Z+WVE3}XZd;{_SiO!fe30oLhVv(~pDOQ@3wbc;pRXgVek7&15WWaFxzzkK{~U>VHVfjji=$;
%gqnDnOAc2V&3;U7JGE^guOGBPx5Zm<5}`N7jKVJ^5XyBEjDqR27+KDO9#jOC6+$zv*e%xsb1IXwr)_?Ywj(U;#p1WsI*Ywm=uF+
CWjbSt`SH4@t|NM*nz0J7mg++@?*#_v-euy&PRH2T3^K_GH2qGFzT;ATM9Y{9p?)A=FLp}6mlj^L}nys(-
QcmZrzqoKd^+|4vL3HM*YDva(^Z`D3tC6DHcn?6iat>dg70RyWmIWstn!ZzI3eM*#|mL~=nZ(#E9a1#p+GLXs%UlvL(OMQ}~C`g{
sM$o%wWp(8?$F5L0u|$G1OnTO#g_n{f=?>ef!5*zgV8x-<?YFt@c`BqNnSAVNEg70mj0sViTvEgkM3Vs4sFD^+V)--
K*GCu4kk8sj$04j|Q?0L<BwSD@%FKZO2V&AbPp3>_ha6#KY?_R*o6hDiE8wW_5RxzFAl>BJa{=~vvf;%E(J%o!HQ4eA<5m>>0Jo;
ah4+{<FUY3o)d5!IJ|Xxp3Mh^3`;2=KlsNB5m-#6=aI18Zz2=+9hg%p!z11hr?p8!Uwmn#H0nNolftq7nPGR7E&YjHmUL-
q5UY2$UgB@*YkZCNGr(-->Er2O=D>gY!GEY?>MZpVR6|42|4mtPH7#fHLv8e$1Qc?KC;C5tcb-HMVZ$U^CT-uYnOF9C0Yp~|t!D-
uce_gd^8{J=m<`E_aKl3QDApAHAo><<<L2!}ccT9BoKDL4`aP84=G(q3|yPxq(sTkS^cqx?r6V}hZuKEPm)5R8ZJ~+pfdPz;@Iq&
l>C4t|DcTvvnktvd<LDtmTtrn!|TBYEr8vY$r9SZNXDld@;WgTm}tnXD8*hSh{_tf_^eI+hrNrbB8-
J2*7<}Hdn4c=b8P4rVvMMTVb_H@UUZ`nxeMCl7UJa}-
x#ygt6!3XBD)Kgl750=ST<{lP{YHdaDt5tf^XQj*=*sjLAp#6JAju(xeJ9h``dFh4MK^VXt5!Qfbq;gaeq6|cmmSJ%{KgHJ=wp@c
`S@#bKyr#Q!bU79gi)s-Xk25F2v2Mm-
I1FWdZAH<uN6#KQuxVATht<3c_T?^IU0<Mbnu|Zs3E{eUv8D(cIxjMmaohvO?Nub+itsy9mS8L(bl;~*ph)&A>px_8zUS?RQ$I?a
b?SrZcd7Haged#&l;&5cXN(q`xTSodlfPw?zjd;#wL9d>IeUzdlhHWEV5(j?ZzebIgndqVSr0?8xvy;)GQXMe*C?h^tWLu8HS`Xa
8!o89+$?-x7<SnNNwl3}gyjQ7!<55-
U%(%`BoMN)B)*4|@W&`=r1Cww`SC6#e7SKW#`_E67<X|Ac56inv8}!Uag#;LS1V2fsnVT?ty~Bv!oZJ2UU|+SH%@N+BT!2N1QY-
O00;m803iSX{BTpr0000a0ssIQ0000_aAj^mXJu}5Ole{-Utei%X>?y-E^v8`kv$8-
Kn#ZW{)$jHK@oIv^AkjiVmr8=*R%%Cq~4vP|K0;Xz~$<aK=LHK$=iW^H$U_?q>&x=Rwc5hiqMWBTNO!~rrQR2Qin1aIzlBDX4m7I
d}t*}W#tV0ow?S;?=)2ofzFLs4_$x`uw2v_mZQP&jej?0bSHLkI8&@@wEgWQN9Ra5ju%o&j`kMriGx3y-
GW1GnfNIAOUH&P)DLZ1RVa-oF(ulTKNKQnPOed2pW@^mT_eHFmuXRSChYO<TORfVP)h*<6ay3h000O8001EX0qK(fRRRD2sR#f73
;+NC0000000000qyYc`002!xRYFB}Wo~pXaCuNm0Rj{Q6aWAK2mk;8AplA)u|TmD008Jx0015U0000000000005)`e*ypiPjF>!L
1$%dbWCYtFGFu`bY*ySQ)O~?X=7zBaCuNm0Rj{Q6aWAK2mk;8ApnYRR#t5b005UF000>P0000000000005)`Y!?6kPjF>!L1$%db
WCYtFHC7>Wn+0`Y-KKRc~DCM0u%!j000080000X0IJ|_jxquO0HFl{03iSX00000000000HgsBBLDzTaAj^mXJu}5Ole{-
O<`_fXJv9PPeD^<b8~5LZZ2?nP)h*<6ay3h000O8001EXj1RN+WE%hgNrV6Z9{>OV0000000000qyd2?002*LWo|)dWo~p#X<{!;
VQyh(WpXc5Wpi_BZ*DGdc~DCM0u%!j000080000X04A&kIXnOW0A2t903ZMW00000000000HgsTK>z?xaAj^mXJu}5Ole{-
O<`_fXJv9PUtei%X>?y-
E^v8JO928D0~7!N00;m803iT#U3Tid0ssKc2mk;d00000000000001_0h~bq08embZb4^dZgfm(VlPi{Wo|)dWo~p$X?SUFb1ras
P)h*<6ay3h000O8001EXCj~M8q7485A~pa38~^|S0000000000qyd&h002*LWo|)dWo~p#X<{!>Y+++%Xm4y}WpZ;aaCuNm0Rj{Q
6aWAK2mk;8ApjW@300g7007P|001EX0000000000005)`a#8>QPjF>!L1$%dbWCYtFHmfCXK8LPP;7N)X>LMcb7d}Yc~DCM0u%!j
000080000X0MCh{nKEnu095$_03-ka00000000000Hgs;UjP74aAj^mXJu}5Ole{-
P;7N)X>Ko2Y;|X8ZgWL$XK8L_E^v8JO928D0~7!N00;m803iV11(lVt7ytmQegFU+00000000000001_0l~`v08embZb4^dZgfm(
VlPr<b8v5Nb7etiWo~pXaCuNm0Rj{Q6aWAK2mk;8AppbZhCMF<000C6001xm0000000000005)`t>gdzPjF>!L1$%dbWCYtFH?DQ
bY*Q&Y;|X8ZgVd~Z)9aJVRUq1V`yJ;Wpj0GbS`jtP)h*<6ay3h000O8001EX8IKJrL;(N*Gy(tsG5`Po0000000000qyZ}C002*L
Wo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FGFu+WiMlBZ*OyDUuJ1+Wo}_@WiD`eP)h*<6ay3h000O8001EXDT#UsO#uJ^I|2XzFaQ7m
0000000000qyfI?002*LWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FGFu+WiMxCZe?;|bY)*=X>4UKaCuNm0Rj{Q6aWAK2mk;8ApmAk
^&2_?0012V001`t0000000000005)`S?K@(PjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVd~Z)9aJXJu|>a$$63Uu|P`Vqa}<WOZz1
E^v8JO928D0~7!N00;m803iT+0*G=S0RRBO0RR9j00000000000001_0qE)g08embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bLvLhd
FLGsJWM5=&V{<NWc~DCM0u%!j000080000X0Oy9YdL{t?0PX<*04o3h00000000000Hgs?>;M2yaAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1y@0ZggdMbT4CUWnpqIaCuNm0Rj{Q6aWAK2mk;8Apit-kl#N6000>R001oj0000000000005)`!0iA4PjF>!
L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVd~Z*FvDcyuphX>(&?a%3)Wc~DCM0u%!j000080000X00V99`XK=T0PX<*05bpp0000000000
0Hgs*?*IT#aAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1y@0ZggdMbT4gXWNBevV{dMBWq5QhaCuNm0Rj{Q6aWAK2mk;8ApjCY^#@%600374001ih0000000000005)`
yzl@3PjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVd~Z*FvDcyupta&>NHE^v8JO928D0~7!N00;m803iTNNl3#r0RR980ssIo00000
000000001_0b=q108embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bLvL<$Wq5Qia%E>_Ze?;|bY(7Zc~DCM0u%!j000080000X08VGU
^fCbe00;sA04@Lk00000000000Hgus^8f%(aAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1y@0ZggdMbT4vcZDnm@WpXZXc~DCM0u%!j000080000X0C#((#3BIz0Pz6;05bpp00000000000Hgt9^#A}*
aAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1y@0ZggdMbT4vcaBO*BV{dMBWq5QhaCuNm0Rj{Q6aWAK2mk;8Apo5uhJUjG000dG001!n0000000000005)`
*7g7ZPjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVd~Z*FvDcyupxZ*Od0Z*_EVb#yLpc~DCM0u%!j000080000X0Kj0#R8Ii_04o9j
05Sjo00000000000Hguf_y7P;aAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1zeCX>4qBL1$%dbT46JbZK^BbY(7Zc~DCM0u%!j000080000X0CB5qO*;Vq01*NJ05bpp00000000000HgtT
`Tzh=aAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1zeCX>4qBL1$%dbT4IiaBp&SUu|SAaCuNm0Rj{Q6aWAK2mk;8AppOq+R8Km000XD001)p0000000000005)`
1N;C0PjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVeFYiVq3b3tciZgekcZE$aLbYE>`E^v8JO928D0~7!N00;m803iS*#dYjF0RR9Q
0ssIp00000000000001_0f_wo08embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bQ)_8#Y;!?pWo~pYX>N0LVQg$JaCuNm0Rj{Q6aWAK
2mk;8Apk#3%;_Bg007bf001rk0000000000005)`6aN4JPjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVeFYiVq3b3tciZgekfX>)Wg
aCuNm0Rj{Q6aWAK2mk;8ApoltECV$G00095001rk0000000000005)`d;kFePjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVeFYiVq3
b3tciZgeklWnpA4aCuNm0Rj{Q6aWAK2mk;8ApoSlo`Wp`008g-
001)p0000000000005)`{Q&_0PjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVeFYiVq3b3tciZgeklWpHm_Y-
w|JE^v8JO928D0~7!N00;m803iTJZs*ZS0RR9f0ssIm00000000000001_0eb@h08embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bQ)
_8#Y;!?pWo~pYb76L6E^v8JO928D0~7!N00;m803iU|fZrKJ0RR9P0ssIu00000000000001_0T2ZN08embZb4^dZgfm(VlPv9b9
7~GP;7N)X>M~bQ)_8#Y;!?pWo~pYb76L6UuJS|ZC_z&E^v8JO928D0~7!N00;m803iTbW)J{90RR9G0ssIj00000000000001_0j
LH608embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bRA^~#YiVw0FK%yiWiD`eP)h*<6ay3h000O8001EXfuX;4A^`vZ(g6SfCIA2c00
00000000qya7n0RT^MWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FH~=2Z!ckFWG--dP)h*<6ay3h000O8001EXzcTa#7XbhO!vO#QC;
$Ke0000000000qydx(0RT^MWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FH~=2Z!cqPWnpqIaCuNm0Rj{Q6aWAK2mk;8App{=4AUwB00
83w001Ze0000000000005)`@d^O|PjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVeGZ)9&TV{C78WiD`eP)h*<6ay3h000O8001EXlw
c36836zQ#{mEUD*ylh0000000000qyb?J0RT^MWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FH~=2Z!cqPZ*yf~Y-
}!Yc~DCM0u%!j000080000X0Iy#~WEueg0L%dZ04e|g00000000000HguK4FLd8aAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1zhHWN$BHb#iiLZgehic~DCM0u%!j000080000X01op32_yjk0Neop04V?f00000000000HgsW4*>vAaAj^m
XJu}5Ole{-Q+acAWo=Mwb!TaAb1zhHWN$BIWo%`1WiD`eP)h*<6ay3h000O8001EXbHP{%DFFZg-vIysCjbBd0000000000qydl+
0RT^MWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FH~=2Z!cwJX>=}dc~DCM0u%!j000080000X09wgHbs+%&0Nw!r051Rl0000000000
0Hgu_5di>CaAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1zkNX>4h9c`spSWo~p|Y;R{SaCuNm0Rj{Q6aWAK2mk;8Apm33Q1vDO007?s001xm0000000000005)`Y!d+h
PjF>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVeHbZKm9ba^jja&m8SUuJ1+WiD`eP)h*<6ay3h000O8001EXlvm5aI{^Ry2Lb>9FaQ7m
0000000000qygX*0RT^MWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FI9ADY-
x0PFKlUZbYFCDZ)|feaCuNm0Rj{Q6aWAK2mk;8ApmcES&=CL008R&001%o0000000000005)`X%+zhPjF>!L1$%dbWCYtFH?DQbY
*Q&Y;|X8ZgVeHbZKm9ba^juY+++%Xm4y}WpZ;aaCuNm0Rj{Q6aWAK2mk;8Apj6&hP+<^002}1001!n0000000000005)`;uiq`Pj
F>!L1$%dbWCYtFH?DQbY*Q&Y;|X8ZgVeHbZKm9ba^juY;|X8ZeL_?V{<NWc~DCM0u%!j000080000X0Arq`izopA0P6t&05t#r00
000000000Hgts836!KaAj^mXJu}5Ole{-
Q+acAWo=Mwb!TaAb1zkNX>4h9c`tHdZe(w5Uvy<{aBN|8WiD`eP)h*<6ay3h000O8001EX6!d3!Dggih>;V7(F#rGn0000000000
qyY;X0RT^MWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FI9ADY-x0PFLZBfWo}<}b75y?E^v8JO928D0~7!N00;m803iS-
7Yb8V0RR9v0ssIn00000000000001_0fZa@08embZb4^dZgfm(VlPv9b97~GP;7N)X>M~bRdi`=X>@rnbZ>8LUub1)a4v9pP)h*<
6ay3h000O8001EXX__o)qyPW_CIJ8dCIA2c0000000000qyZ)#0RT^MWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FJE72ZfSI1UoLQY
P)h*<6ay3h000O8001EXF4PALD+>Ss4krKrA^-
pY0000000000qyY{e0RT^MWo|)dWo~p#X<{!^d2@7SZBT4=XK8M8FJfVHWiD`eP)h*<6ay3h000O8001EX2V-
wVzXkvR+!+7>8vp<R0000000000qyc#<0RT^MWo|)dWo~p#X<{!_Z)9&%WpZ|DV`VOIc~DCM0u%!j000080000X0M^GHN)9mq0Q<
`T02}}S00000000000HgtNF#!NiaAj^mXJu}5Ole{-
RBvx=L}_zyVRU0?E^v8JO928D0~7!N00;m803iSX{BTpr0000a0ssIQ00000000000001_0l8uU08embZb4^dZgfm(VlQ7`X>MtB
Utcb8c~DCQ1^@s605$+N0D%$!0JviT0000
"""

def __cubkit_bootstrap__():
    # CubKit import-debug: this function is generated by CubKit.
    # It prepares bundled files before the real MCUB module code below runs.
    import base64
    import hashlib
    import os
    import sys
    import types
    import zipfile
    from pathlib import Path

    # CubKit import-debug: decode the embedded base85 zip payload.
    data = base64.b85decode("".join(__cubkit_bundle_b85__.split()).encode("ascii"))
    digest = hashlib.sha256(data).hexdigest()
    # CubKit import-debug: fail fast if the embedded payload was corrupted.
    if digest != __cubkit_bundle_sha256__:
        raise RuntimeError("CubKit embedded bundle checksum mismatch")

    # CubKit import-debug: cache extraction avoids rewriting helper files on every import.
    cache_root = Path(os.environ.get("CUBKIT_CACHE_DIR", Path.home() / ".cache" / "cubkit"))
    bundle_dir = cache_root / __cubkit_module_id__ / digest
    marker = bundle_dir / ".cubkit-extracted"
    if not marker.exists():
        bundle_dir.mkdir(parents=True, exist_ok=True)
        archive_path = bundle_dir / "bundle.zip"
        archive_path.write_bytes(data)
        with zipfile.ZipFile(archive_path) as archive:
            archive.extractall(bundle_dir)
        marker.write_text(digest, encoding="utf-8")

    # CubKit import-debug: expose extracted top-level files for normal absolute imports.
    bundle_path = str(bundle_dir)
    if bundle_path not in sys.path:
        sys.path.insert(0, bundle_path)

    # CubKit import-debug: build private package search paths for `from .utils import ...`.
    relative_import_paths = [bundle_path]
    for package_dir in reversed(__cubkit_package_dirs__):
        package_path = bundle_dir / package_dir
        if package_path.is_dir():
            relative_import_paths.insert(0, str(package_path))

    # CubKit import-debug: mark the generated main module as package-like.
    # This prevents accidental imports from global MCUB packages named `utils`, `lib`, etc.
    module_globals = globals()
    module_globals["__path__"] = relative_import_paths
    module_globals["__package__"] = module_globals.get("__name__", __cubkit_module_id__)
    module_spec = module_globals.get("__spec__")
    if module_spec is not None:
        module_spec.submodule_search_locations = relative_import_paths

    # CubKit import-debug: expose vendored libraries through `from cubkit.lib import name`.
    lib_path = bundle_dir / __cubkit_lib_dir__
    if lib_path.is_dir():
        lib_path_str = str(lib_path)
        if lib_path_str not in sys.path:
            sys.path.insert(0, lib_path_str)

        cubkit_pkg = sys.modules.get("cubkit")
        if cubkit_pkg is None:
            cubkit_pkg = types.ModuleType("cubkit")
            sys.modules["cubkit"] = cubkit_pkg
        if not hasattr(cubkit_pkg, "__path__"):
            cubkit_pkg.__path__ = []

        lib_pkg = sys.modules.get("cubkit.lib")
        if lib_pkg is None:
            lib_pkg = types.ModuleType("cubkit.lib")
            sys.modules["cubkit.lib"] = lib_pkg
        lib_pkg.__path__ = [lib_path_str]
        lib_pkg.__package__ = "cubkit"
        setattr(cubkit_pkg, "lib", lib_pkg)

__cubkit_bootstrap__()
del __cubkit_bootstrap__

# ---- CubKit entrypoint: OpenAgentMain.py ----
# SPDX-License-Identifier: MIT
# scope: heroku_min 9.9.9
# -- repo data --
# repo: https://github.com/hairpin01/repo-MCUB-fork/
# -- end --
# scop: kernel min v1.4.6


import asyncio
import contextlib
import html
import io
import re
import time
import uuid
import json
from pathlib import Path
from typing import Any, TYPE_CHECKING


from core.lib.loader.module_base import ModuleBase, bot_command, callback, command
from core.lib.loader.module_config import (
    Boolean,
    Choice,
    ConfigValue,
    Float,
    Group,
    Row,
    Answer,
    Integer,
    List,
    ModuleConfig,
    Secret,
    String,
)

if TYPE_CHECKING:
    from core.lib.types import InlineMessage, Event

try:
    from OpenAgentLib.OpenAgentMixins import (
        _OpenAgentLifecycleMixin,
        _OpenAgentProviderMixin,
        _OpenAgentTodoMixin,
        _OpenAgentToolDisplayMixin,
        _OpenAgentContextMixin,
        _OpenAgentSessionsMixin,
        _OpenAgentPluginSkillMixin,
        _OpenAgentRuntimeToolsMixin,
        _OpenAgentTelegramMediaMixin,
        _OpenAgentStatusMixin,
        _OpenAgentAgentLoopMixin,
        _OpenAgentResponseMixin,
        _OpenAgentToolRegistryMixin,
    )
except Exception as e:
    raise RuntimeError(e) from e # debug


class OpenAgent(
    _OpenAgentLifecycleMixin,
    _OpenAgentProviderMixin,
    _OpenAgentTodoMixin,
    _OpenAgentToolDisplayMixin,
    _OpenAgentContextMixin,
    _OpenAgentSessionsMixin,
    _OpenAgentPluginSkillMixin,
    _OpenAgentRuntimeToolsMixin,
    _OpenAgentTelegramMediaMixin,
    _OpenAgentStatusMixin,
    _OpenAgentAgentLoopMixin,
    _OpenAgentResponseMixin,
    _OpenAgentToolRegistryMixin,
    ModuleBase,
):
    name = "OpenAgent"
    version = "0.8.0-main.build:1043"
    author = "@dev_dolbaeb && @Hairpin00"
    description = {
        "ru": "ИИ агент в юзерботе с новой архитектурой инструментов",
        "en": "AI agent in userbot with refreshed tool architecture",
        "rofl": "ИИ агент, который делает вид, что всё контролирует",
        "linux": "AI agent daemon with tool-oriented runtime",
    }
    strings = {
        "ru": {
            "need_text": "Usage: .oa <request>",
            "thinking": "Thinking...",
            "running_terminal": "Running terminal command...",
            "running_search": "Searching the web...",
            "no_key": "API key is not configured. Use .cfg OpenAgent api_key",
            "bad_provider": "Unknown provider. Available: {providers}",
            "provider_saved": "Provider saved: {provider}",
            "key_saved": "Provider and API key saved: {provider}",
            "disabled": "Provider {provider} is not available yet",
            "error": "OpenAgent error: {error}",
            "thinking_empty_text": "Модель ещё не думала.",
            "thinking_template_default": '<blockquote><a href="tg://emoji?id=6010292571627069263">😎</a> <u>{provider}/{model}</u> • <em>prepares the response...</em></blockquote >\n<blockquote><a href="tg://emoji?id=5404857686477015710">🔄</a><strong><em> {random}</em></strong><em></em></blockquote>',
            "request_label_default": '<a href="tg://emoji?id=6010352868672936598"><strong>🐈‍⬛</strong></a><strong></strong><strong> Prompt:</strong>',
            "response_label_default": '<a href="tg://emoji?id=6010286885090368072"><strong>❌</strong></a><strong></strong><strong> Answer:</strong>',
            "agent_log_label": "Agent Log",
            "status_thinking": "Думаю",
            "status_terminal": "Выполняю команду",
            "status_web": "Работаю с web",
            "status_file": "Работаю с файлом",
            "status_mcub": "Выполняю MCUB-команду",
            "status_message": "Работаю с сообщениями",
            "status_chat": "Проверяю чат",
            "status_dialog": "Проверяю диалоги",
            "status_code": "Готовлю код",
            "status_todo": "Обновляю TODO",
            "status_default": "Выполняю {tool}",
            "tool_confirmation_approved": "Выполняю",
            "tool_confirmation_yes_text": "Выполнить",
            "tool_confirmation_no_text": "Не сейчас",
            "tool_validation_retry_prompt": "Это результат валидации твоего tool_call. Исправь tool_call и повтори прямо сейчас. Fix the tool call and try again now. Use only valid OpenAgent tool names, valid JSON, and args as a JSON object. If no tool is needed, answer the user in plain text with no JSON/tool_call.",
            "runtime_comment_button": "💬 Комментировать",
            "runtime_comment_placeholder": "Комментарий агенту...",
            "runtime_comment_saved": "Комментарий добавлен",
            "runtime_comment_note": "Пользователь добавил комментарий во время выполнения. Учти это в следующих шагах:\n{comments}",
            "follow_up_button": "✍️ Продолжить",
            "follow_up_placeholder": "Введи запрос...",
            "regen_prompt_button": "🔁 Реген с промптом",
            "regen_prompt_placeholder": "Новый промпт для регенерации...",
            "regen_stale": "Запрос устарел",
            "regenerating": "Регенерирую...",
            "new_session_name": "Новый чат",
            "chat_history_button": "💬 История чатов",
            "chats_title": "💬 <b>Чаты — этот чат</b>",
            "chat_empty": "Пока нет сообщений",
            "chat_today": "сегодня",
            "chat_yesterday": "вчера",
            "chat_days_ago": "{days} дн назад",
            "new_chat_button": "+ Новый чат",
            "ask_this_chat_button": "✍️ Спросить в этом чате",
            "ask_this_chat_placeholder": "Запрос для этого чата...",
            "return_to_chat_button": "↩️ Вернуться в этот чат",
            "saved_response_missing": "В истории этого чата ещё нет ответа ИИ",
            "rename_chat_button": "✏️ Переименовать",
            "delete_chat_button": "🗑 Удалить",
            "remember_chat_button": "💾 Запомнить выбор",
            "chat_choice_saved": "Выбор запомнен",
            "chat_switched": "Чат активен: {name}",
            "chat_created": "Создан чат: {name}",
            "chat_renamed": "Чат переименован: {name}",
            "chat_deleted": "Чат удалён",
            "chat_delete_last": "Нельзя удалить последний чат",
            "new_chat_placeholder": "Название (или Enter для авто...)",
            "rename_chat_placeholder": "Новое название...",
            "auto_name_prompt": "Придумай короткое название сессии на 3-4 слова. Ответь только названием. Запрос: {prompt}",
            "oa_choose_chat": "Выбери чат для продолжения или создай новый.",
            "fallback_thinking_note": "Понял задачу, начинаю выполнение.",
            "tools_no_final": "Инструменты выполнены, но модель не сформировала финальный текст.",
            "tool_call_bad_json": "Ошибка tool call: модель вернула некорректный JSON ({error}).\nФрагмент: {preview}",
            "tool_call_not_object": "Ошибка tool call: элемент вызова инструмента должен быть JSON-объектом.",
            "tool_call_unknown": "Ошибка tool call: неизвестный инструмент '{tool_name}'.{hint} Доступные примеры: {available}.",
            "tool_call_nearest": " Ближайшие: {nearest}.",
            "tool_call_args_not_object": "Ошибка tool call: args для '{tool_name}' должен быть JSON-объектом.",
            "answer_file_request": "Запрос",
            "answer_file_answer": "Ответ",
            "answer_file_too_long": "<b>Ответ слишком длинный, отправляю файлом.</b>",
            "answer_file_attach_failed": "<b>Не удалось прикрепить файл к форме, показываю начало:</b>",
            "continued": "continued",
            "cancelled": "Отменено",
            "context_cleared": "Контекст очищен",
            "clear_button": "🧹 Очистить",
            "regenerate_button": "🔃 Регенерировать",
            "cancel_button": "Отмена",
            "reply_analyze_prompt": "Проанализируй вложение/сообщение из reply.",
            "skills_empty": "No OpenAgent skills installed",
            "skillinstall_usage": "Usage: .skillinstall <skill_name>",
            "sendss_usage": "Usage: .sendss <skill_name>",
            "skill_not_found": "Skill not found",
            "skill_name_required": "skill name is required",
            "skill_not_found_repo": "Skill not found in repo: {query}",
            "skill_saved": "Skill saved: {name}",
            "unknown_skills_tool": "Unknown skills tool: {tool}",
            "imss_need_reply": "Reply to a .md file or markdown message",
            "skill_empty": "Skill content is empty",
            "delss_usage": "Usage: .delss <skill_name>",
            "skill_installed": "Skill installed: <code>{name}</code>",
            "skill_imported": "Skill imported: <code>{name}</code>",
            "skill_deleted": "Skill deleted: <code>{name}</code>",
            "plugin_install_failed": "Plugin install failed: <code>{error}</code>",
            "plugin_installed": "Plugin installed: <code>{name}</code>",
            "plugins_enabled_title": "<b>🧩 Включёные плагины:</b>\n",
            "plugins_none_installed": "\nНет установленных плагинов\n",
            "plugins_total": "\n<b>Всего плагинов:</b> {count}",
            "plugin_catalog_btn": "📦 Каталог",
            "plugin_manager_btn": "⚙️ Менеджер",
            "close_btn": "❌ Закрыть",
            "plugin_repo_empty": "❌ Нет плагинов в репозитории",
            "plugin_no_description": "Нет описания",
            "plugin_more_tools": " ...и ещё {count}",
            "plugin_tools_label": "Tools",
            "plugin_installed_btn": "✅ Установлен",
            "plugin_install_btn": "📥 Установить",
            "plugin_code_btn": "📄 Код",
            "back_btn": "🔙 Назад",
            "plugin_installing": "⏳ Устанавливаю...",
            "plugin_installed_alert": "✅ {name} установлен!",
            "generic_error": "❌ Ошибка: {error}",
            "plugin_manager_no_installed": "Нет установленных плагинов",
            "plugin_version_label": "Версия",
            "plugin_id_label": "ID",
            "plugin_author_label": "Автор",
            "plugin_permissions_label": "Права",
            "plugin_requirements_label": "Зависимости",
            "plugin_actions_title": "<b>Действия:</b>",
            "plugin_delete_btn": "🗑 Удалить",
            "plugin_deleted_alert": "🗑 {name} удалён",
            "oa_chat_choice_title": "💬 <b>Куда отправить запрос?</b>",
            "remember_pref_continue": "💾 Всегда сюда",
            "remember_pref_new": "💾 Всегда новый",
            "pref_saved": "Запомнено",
        },
        "en": {
            "need_text": "Usage: .oa <request>",
            "thinking": "Thinking...",
            "running_terminal": "Running terminal command...",
            "running_search": "Searching the web...",
            "no_key": "API key is not configured. Use .cfg OpenAgent api_key",
            "bad_provider": "Unknown provider. Available: {providers}",
            "provider_saved": "Provider saved: {provider}",
            "key_saved": "Provider and API key saved: {provider}",
            "disabled": "Provider {provider} is not available yet",
            "error": "OpenAgent error: {error}",
            "thinking_empty_text": "The model has not thought yet.",
            "thinking_template_default": '<blockquote><a href="tg://emoji?id=6010292571627069263">😎</a> <u>{provider}/{model}</u> • <em>prepares the response...</em></blockquote >\n<blockquote><a href="tg://emoji?id=5404857686477015710">🔄</a><strong><em> {random}</em></strong><em></em></blockquote>',
            "request_label_default": '<a href="tg://emoji?id=6010352868672936598"><strong>🐈‍⬛</strong></a><strong></strong><strong> Prompt:</strong>',
            "response_label_default": '<a href="tg://emoji?id=6010286885090368072"><strong>❌</strong></a><strong></strong><strong> Answer:</strong>',
            "agent_log_label": "Agent Log",
            "status_thinking": "Thinking",
            "status_terminal": "Running command",
            "status_web": "Working with web",
            "status_file": "Working with file",
            "status_mcub": "Running MCUB command",
            "status_message": "Working with messages",
            "status_chat": "Checking chat",
            "status_dialog": "Checking dialogs",
            "status_code": "Preparing code",
            "status_todo": "Updating TODO",
            "status_default": "Running {tool}",
            "tool_confirmation_approved": "Running",
            "tool_confirmation_yes_text": "Run",
            "tool_confirmation_no_text": "Not now",
            "tool_validation_retry_prompt": "This is the validation result for your tool_call. Fix the tool call and try again now. Use only valid OpenAgent tool names, valid JSON, and args as a JSON object. If no tool is needed, answer the user in plain text with no JSON/tool_call.",
            "runtime_comment_button": "💬 Comment",
            "runtime_comment_placeholder": "Comment for agent...",
            "runtime_comment_saved": "Comment added",
            "runtime_comment_note": "The user added a live comment while you were working. Use it in the next steps:\n{comments}",
            "follow_up_button": "✍️ Continue",
            "follow_up_placeholder": "Enter request...",
            "regen_prompt_button": "🔁 Regen with prompt",
            "regen_prompt_placeholder": "New prompt for regeneration...",
            "regen_stale": "Request expired",
            "regenerating": "Regenerating...",
            "new_session_name": "New chat",
            "chat_history_button": "💬 Chat history",
            "chats_title": "💬 <b>Chats — this chat</b>",
            "chat_empty": "No messages yet",
            "chat_today": "today",
            "chat_yesterday": "yesterday",
            "chat_days_ago": "{days} days ago",
            "new_chat_button": "+ New chat",
            "ask_this_chat_button": "✍️ Ask in this chat",
            "ask_this_chat_placeholder": "Request for this chat...",
            "return_to_chat_button": "↩️ Return to this chat",
            "saved_response_missing": "This chat history has no AI answer yet",
            "rename_chat_button": "✏️ Rename",
            "delete_chat_button": "🗑 Delete",
            "remember_chat_button": "💾 Remember choice",
            "chat_choice_saved": "Choice remembered",
            "chat_switched": "Active chat: {name}",
            "chat_created": "Created chat: {name}",
            "chat_renamed": "Chat renamed: {name}",
            "chat_deleted": "Chat deleted",
            "chat_delete_last": "Cannot delete the last chat",
            "new_chat_placeholder": "Name (or Enter for auto...)",
            "rename_chat_placeholder": "New name...",
            "auto_name_prompt": "Create a short 3-4 word session title. Reply with the title only. Request: {prompt}",
            "oa_choose_chat": "Choose a chat to continue or create a new one.",
            "fallback_thinking_note": "Understood the task, starting execution.",
            "tools_no_final": "Tools ran, but the model did not provide final text.",
            "tool_call_bad_json": "Tool call error: model returned invalid JSON ({error}).\nFragment: {preview}",
            "tool_call_not_object": "Tool call error: tool call item must be a JSON object.",
            "tool_call_unknown": "Tool call error: unknown tool '{tool_name}'.{hint} Available examples: {available}.",
            "tool_call_nearest": " Nearest: {nearest}.",
            "tool_call_args_not_object": "Tool call error: args for '{tool_name}' must be a JSON object.",
            "answer_file_request": "Request",
            "answer_file_answer": "Answer",
            "answer_file_too_long": "<b>Answer is too long, sending it as a file.</b>",
            "answer_file_attach_failed": "<b>Failed to attach the file to the form, showing the beginning:</b>",
            "continued": "continued",
            "cancelled": "Cancelled",
            "context_cleared": "Context cleared",
            "clear_button": "🧹 Clear",
            "regenerate_button": "🔃 Regenerate",
            "cancel_button": "Cancel",
            "reply_analyze_prompt": "Analyze the replied attachment/message.",
            "skills_empty": "No OpenAgent skills installed",
            "skillinstall_usage": "Usage: .skillinstall <skill_name>",
            "sendss_usage": "Usage: .sendss <skill_name>",
            "skill_not_found": "Skill not found",
            "skill_name_required": "skill name is required",
            "skill_not_found_repo": "Skill not found in repo: {query}",
            "skill_saved": "Skill saved: {name}",
            "unknown_skills_tool": "Unknown skills tool: {tool}",
            "imss_need_reply": "Reply to a .md file or markdown message",
            "skill_empty": "Skill content is empty",
            "delss_usage": "Usage: .delss <skill_name>",
            "skill_installed": "Skill installed: <code>{name}</code>",
            "skill_imported": "Skill imported: <code>{name}</code>",
            "skill_deleted": "Skill deleted: <code>{name}</code>",
            "plugin_install_failed": "Plugin install failed: <code>{error}</code>",
            "plugin_installed": "Plugin installed: <code>{name}</code>",
            "plugins_enabled_title": "<b>🧩 Enabled plugins:</b>\n",
            "plugins_none_installed": "\nNo installed plugins\n",
            "plugins_total": "\n<b>Total plugins:</b> {count}",
            "plugin_catalog_btn": "📦 Catalog",
            "plugin_manager_btn": "⚙️ Manager",
            "close_btn": "❌ Close",
            "plugin_repo_empty": "❌ No plugins in repository",
            "plugin_no_description": "No description",
            "plugin_more_tools": " ...and {count} more",
            "plugin_tools_label": "Tools",
            "plugin_installed_btn": "✅ Installed",
            "plugin_install_btn": "📥 Install",
            "plugin_code_btn": "📄 Code",
            "back_btn": "🔙 Back",
            "plugin_installing": "⏳ Installing...",
            "plugin_installed_alert": "✅ {name} installed!",
            "generic_error": "❌ Error: {error}",
            "plugin_manager_no_installed": "No installed plugins",
            "plugin_version_label": "Version",
            "plugin_id_label": "ID",
            "plugin_author_label": "Author",
            "plugin_permissions_label": "Permissions",
            "plugin_requirements_label": "Requirements",
            "plugin_actions_title": "<b>Actions:</b>",
            "plugin_delete_btn": "🗑 Delete",
            "plugin_deleted_alert": "🗑 {name} deleted",
            "oa_chat_choice_title": "💬 <b>Where to send the request?</b>",
            "remember_pref_continue": "💾 Always here",
            "remember_pref_new": "💾 Always new",
            "pref_saved": "Remembered",
        },
        "rofl": {
            "need_text": "кинь промпт: .oa <запрос>",
            "thinking": "мозг греется...",
            "running_terminal": "консоль делает бррр...",
            "running_search": "гуглю мемы...",
            "no_key": "ключика нет, брат. .cfg OpenAgent api_key",
            "bad_provider": "такого провайдера не завезли. Есть: {providers}",
            "provider_saved": "провайдер запомнен: {provider}",
            "key_saved": "провайдер и ключ сохранены: {provider}",
            "disabled": "провайдер {provider} пока в отпуске",
            "error": "OpenAgent словил прикол: {error}",
            "thinking_empty_text": "нейронка пока делает вид, что думает.",
            "thinking_template_default": '<blockquote><a href="tg://emoji?id=6010292571627069263">😎</a> <u>{provider}/{model}</u> • <em>варит ответ...</em></blockquote >\n<blockquote><a href="tg://emoji?id=5404857686477015710">🔄</a><strong><em> {random}</em></strong><em></em></blockquote>',
            "request_label_default": '<a href="tg://emoji?id=6010352868672936598"><strong>🐈‍⬛</strong></a><strong></strong><strong> Промптик:</strong>',
            "response_label_default": '<a href="tg://emoji?id=6010286885090368072"><strong>❌</strong></a><strong></strong><strong> Ответик:</strong>',
            "agent_log_label": "Лог движухи",
            "status_thinking": "Думаю, мамой клянусь",
            "status_terminal": "Терминалю",
            "status_web": "Шарюсь в интернетах",
            "status_file": "Щупаю файл",
            "status_mcub": "Дёргаю MCUB",
            "status_message": "Кручу сообщения",
            "status_chat": "Смотрю чатик",
            "status_dialog": "Листаю диалоги",
            "status_code": "Пишу код без паники",
            "status_todo": "Туда-сюда TODO",
            "status_default": "Делаю {tool}",
            "tool_confirmation_approved": "Ща сделаю",
            "tool_confirmation_yes_text": "Вжухнуть",
            "tool_confirmation_no_text": "Не щас",
            "tool_validation_retry_prompt": "Это результат проверки tool_call. Почини tool_call и повтори прямо сейчас. Используй только валидные OpenAgent tool names, валидный JSON и args как JSON object. Если инструмент не нужен — отвечай текстом без JSON/tool_call.",
            "runtime_comment_button": "💬 Подкинуть мысль",
            "runtime_comment_placeholder": "Вкинь коммент агенту...",
            "runtime_comment_saved": "Коммент долетел",
            "runtime_comment_note": "Юзер подкинул коммент пока ты работал. Учти дальше:\n{comments}",
            "follow_up_button": "✍️ Ещё вопросик",
            "follow_up_placeholder": "Вкидывай запрос...",
            "regen_prompt_button": "🔁 Переварить с промптом",
            "regen_prompt_placeholder": "Новый промпт для переварки...",
            "regen_stale": "Запрос протух",
            "regenerating": "Переварю ещё раз...",
            "new_session_name": "Новый чатик",
            "chat_history_button": "💬 Чатики",
            "chats_title": "💬 <b>Чаты — тут</b>",
            "chat_empty": "пока пусто, как в голове",
            "chat_today": "сегодня",
            "chat_yesterday": "вчерась",
            "chat_days_ago": "{days} дн назад",
            "new_chat_button": "+ Новый чатик",
            "ask_this_chat_button": "✍️ Спросить тут",
            "ask_this_chat_placeholder": "Вкидывай запрос в этот чатик...",
            "return_to_chat_button": "↩️ Вернуться в чатик",
            "saved_response_missing": "В истории чатка ещё нет ответа ИИ",
            "rename_chat_button": "✏️ Переобозвать",
            "delete_chat_button": "🗑 Снести",
            "remember_chat_button": "💾 Запомнить прикол",
            "chat_choice_saved": "Запомнил, начальник",
            "chat_switched": "Теперь активен: {name}",
            "chat_created": "Чатик создан: {name}",
            "chat_renamed": "Чатик переобозван: {name}",
            "chat_deleted": "Чатик снесён",
            "chat_delete_last": "Последний чатик не дам снести",
            "new_chat_placeholder": "Название (или Enter для авто...)",
            "rename_chat_placeholder": "Новое имя чатика...",
            "auto_name_prompt": "Придумай мемное короткое название сессии на 3-4 слова. Ответь только названием. Запрос: {prompt}",
            "oa_choose_chat": "Выбери чатик или создай новый.",
            "fallback_thinking_note": "Задачу понял, погнали.",
            "tools_no_final": "Инструменты отработали, а модель финал зажала.",
            "tool_call_bad_json": "tool call кринжанул JSON ({error}).\nФрагмент: {preview}",
            "tool_call_not_object": "tool call должен быть JSON-объектом, не приколом.",
            "tool_call_unknown": "не знаю инструмент '{tool_name}'.{hint} Примеры: {available}.",
            "tool_call_nearest": " Похоже на: {nearest}.",
            "tool_call_args_not_object": "args для '{tool_name}' должны быть JSON-объектом.",
            "answer_file_request": "Запросик",
            "answer_file_answer": "Ответик",
            "answer_file_too_long": "<b>Ответ жирный, кидаю файлом.</b>",
            "answer_file_attach_failed": "<b>Файл не прилепился, показываю начало:</b>",
            "continued": "продолжение банкета",
            "cancelled": "Отменено, расходимся",
            "context_cleared": "Контекст помыт",
            "clear_button": "🧹 Стереть",
            "regenerate_button": "🔃 Переварить",
            "cancel_button": "Стопэ",
            "reply_analyze_prompt": "Глянь вложение/сообщение из reply.",
            "skills_empty": "Скиллов OpenAgent нет, пустота",
            "skillinstall_usage": "Юзай: .skillinstall <skill_name>",
            "sendss_usage": "Юзай: .sendss <skill_name>",
            "skill_not_found": "Скилл потерялся",
            "skill_name_required": "нужно имя скилла",
            "skill_not_found_repo": "Скилл в репе потерялся: {query}",
            "skill_saved": "Скилл сохранён: {name}",
            "unknown_skills_tool": "Неизвестный скилл-инструмент: {tool}",
            "imss_need_reply": "Ответь на .md файл или markdown сообщение",
            "skill_empty": "Скилл пустой как холодильник",
            "delss_usage": "Юзай: .delss <skill_name>",
            "skill_installed": "Скилл установлен: <code>{name}</code>",
            "skill_imported": "Скилл импортнут: <code>{name}</code>",
            "skill_deleted": "Скилл удалён: <code>{name}</code>",
            "plugin_install_failed": "Плагин не взлетел: <code>{error}</code>",
            "plugin_installed": "Плагин залетел: <code>{name}</code>",
            "plugins_enabled_title": "<b>🧩 Включёные плагины:</b>\n",
            "plugins_none_installed": "\nПлагинов ноль, грустно\n",
            "plugins_total": "\n<b>Всего плагинов:</b> {count}",
            "plugin_catalog_btn": "📦 Склад",
            "plugin_manager_btn": "⚙️ Рулёжка",
            "close_btn": "❌ Закрыть лавочку",
            "plugin_repo_empty": "❌ В репе плагинов кот наплакал",
            "plugin_no_description": "Описание украли",
            "plugin_more_tools": " ...и ещё {count} сверху",
            "plugin_tools_label": "Инструменты",
            "plugin_installed_btn": "✅ Уже стоит",
            "plugin_install_btn": "📥 Вкатить",
            "plugin_code_btn": "📄 Кодец",
            "back_btn": "🔙 Назад",
            "plugin_installing": "⏳ Вкатываю...",
            "plugin_installed_alert": "✅ {name} вкатился!",
            "generic_error": "❌ Ошибочка: {error}",
            "plugin_manager_no_installed": "Плагинов нет",
            "plugin_version_label": "Версия",
            "plugin_id_label": "ID",
            "plugin_author_label": "Автор",
            "plugin_permissions_label": "Права",
            "plugin_requirements_label": "Зависимости",
            "plugin_actions_title": "<b>Движения:</b>",
            "plugin_delete_btn": "🗑 Снести",
            "plugin_deleted_alert": "🗑 {name} снесён",
            "oa_chat_choice_title": "💬 <b>Куда кидаем запрос?</b>",
            "remember_pref_continue": "💾 Всегда тут",
            "remember_pref_new": "💾 Всегда новый",
            "pref_saved": "Запомнил, бро",
        },
        "linux": {
            "need_text": "usage: .oa <request>",
            "thinking": "forking thoughts...",
            "running_terminal": "execve(command)...",
            "running_search": "resolving web query...",
            "no_key": "api_key: ENOENT. Set .cfg OpenAgent api_key",
            "bad_provider": "provider: EINVAL. Available: {providers}",
            "provider_saved": "provider={provider} written",
            "key_saved": "provider={provider} and api_key written",
            "disabled": "provider {provider}: ENOSYS",
            "error": "openagent: {error}",
            "thinking_empty_text": "no reasoning frames in buffer.",
            "thinking_template_default": '<blockquote><a href="tg://emoji?id=6010292571627069263">😎</a> <u>{provider}/{model}</u> • <em>spawning response...</em></blockquote >\n<blockquote><a href="tg://emoji?id=5404857686477015710">🔄</a><strong><em> {random}</em></strong><em></em></blockquote>',
            "request_label_default": '<a href="tg://emoji?id=6010352868672936598"><strong>🐈‍⬛</strong></a><strong></strong><strong> stdin:</strong>',
            "response_label_default": '<a href="tg://emoji?id=6010286885090368072"><strong>❌</strong></a><strong></strong><strong> stdout:</strong>',
            "agent_log_label": "syslog",
            "status_thinking": "reasoning",
            "status_terminal": "exec command",
            "status_web": "net I/O",
            "status_file": "file I/O",
            "status_mcub": "mcub syscall",
            "status_message": "message I/O",
            "status_chat": "stat chat",
            "status_dialog": "scan dialogs",
            "status_code": "compile code",
            "status_todo": "sync TODO",
            "status_default": "run {tool}",
            "tool_confirmation_approved": "executing",
            "tool_confirmation_yes_text": "exec",
            "tool_confirmation_no_text": "skip",
            "tool_validation_retry_prompt": "tool_call validation output. Fix the tool call and retry now. Use only valid OpenAgent tool names, valid JSON, and args as a JSON object. If no tool is needed, answer the user in plain text with no JSON/tool_call.",
            "runtime_comment_button": "💬 stdin+",
            "runtime_comment_placeholder": "append runtime comment...",
            "runtime_comment_saved": "comment queued",
            "runtime_comment_note": "Runtime user comment received. Apply it in next steps:\n{comments}",
            "follow_up_button": "✍️ stdin",
            "follow_up_placeholder": "type request...",
            "regen_prompt_button": "🔁 rerun stdin",
            "regen_prompt_placeholder": "new rerun prompt...",
            "regen_stale": "request expired",
            "regenerating": "rerunning...",
            "new_session_name": "new-chat",
            "chat_history_button": "💬 sessions",
            "chats_title": "💬 <b>sessions — current tty</b>",
            "chat_empty": "empty buffer",
            "chat_today": "today",
            "chat_yesterday": "yesterday",
            "chat_days_ago": "{days}d ago",
            "new_chat_button": "+ fork session",
            "ask_this_chat_button": "✍️ stdin to this session",
            "ask_this_chat_placeholder": "stdin for this session...",
            "return_to_chat_button": "↩️ return to this session",
            "saved_response_missing": "session history has no assistant stdout yet",
            "rename_chat_button": "✏️ mv session",
            "delete_chat_button": "🗑 rm session",
            "remember_chat_button": "💾 persist choice",
            "chat_choice_saved": "choice persisted",
            "chat_switched": "active session: {name}",
            "chat_created": "session created: {name}",
            "chat_renamed": "session renamed: {name}",
            "chat_deleted": "session removed",
            "chat_delete_last": "cannot remove last session",
            "new_chat_placeholder": "name (or Enter for auto...)",
            "rename_chat_placeholder": "new name...",
            "auto_name_prompt": "Create a short 3-4 word session title. Reply with the title only. Request: {prompt}",
            "oa_choose_chat": "select a session to continue or fork a new one.",
            "fallback_thinking_note": "task accepted; starting worker.",
            "tools_no_final": "tools exited 0, final output is empty.",
            "tool_call_bad_json": "tool_call: JSON parse failed ({error}).\nFragment: {preview}",
            "tool_call_not_object": "tool_call: item must be a JSON object.",
            "tool_call_unknown": "tool_call: unknown executable '{tool_name}'.{hint} Examples: {available}.",
            "tool_call_nearest": " Did you mean: {nearest}.",
            "tool_call_args_not_object": "tool_call: args for '{tool_name}' must be a JSON object.",
            "answer_file_request": "stdin",
            "answer_file_answer": "stdout",
            "answer_file_too_long": "<b>stdout too large, redirecting to file.</b>",
            "answer_file_attach_failed": "<b>attach failed, dumping head:</b>",
            "continued": "continued",
            "cancelled": "SIGTERM sent",
            "context_cleared": "context buffer cleared",
            "clear_button": "🧹 clear",
            "regenerate_button": "🔃 rerun",
            "cancel_button": "SIGTERM",
            "reply_analyze_prompt": "Analyze replied attachment/message.",
            "skills_empty": "No OpenAgent skills installed",
            "skillinstall_usage": "usage: .skillinstall <skill_name>",
            "sendss_usage": "usage: .sendss <skill_name>",
            "skill_not_found": "skill: ENOENT",
            "skill_name_required": "skill name is required",
            "skill_not_found_repo": "skill repo lookup failed: {query}",
            "skill_saved": "skill saved: {name}",
            "unknown_skills_tool": "unknown skills tool: {tool}",
            "imss_need_reply": "reply to a .md file or markdown message",
            "skill_empty": "skill content is empty",
            "delss_usage": "usage: .delss <skill_name>",
            "skill_installed": "skill installed: <code>{name}</code>",
            "skill_imported": "skill imported: <code>{name}</code>",
            "skill_deleted": "skill deleted: <code>{name}</code>",
            "plugin_install_failed": "plugin install failed: <code>{error}</code>",
            "plugin_installed": "plugin installed: <code>{name}</code>",
            "plugins_enabled_title": "<b>🧩 loaded plugins:</b>\n",
            "plugins_none_installed": "\nno loaded plugins\n",
            "plugins_total": "\n<b>plugin count:</b> {count}",
            "plugin_catalog_btn": "📦 catalog",
            "plugin_manager_btn": "⚙️ systemctl",
            "close_btn": "❌ close",
            "plugin_repo_empty": "❌ repository index is empty",
            "plugin_no_description": "no description",
            "plugin_more_tools": " ...and {count} more",
            "plugin_tools_label": "Tools",
            "plugin_installed_btn": "✅ loaded",
            "plugin_install_btn": "📥 install",
            "plugin_code_btn": "📄 source",
            "back_btn": "🔙 back",
            "plugin_installing": "⏳ installing package...",
            "plugin_installed_alert": "✅ {name} installed!",
            "generic_error": "❌ error: {error}",
            "plugin_manager_no_installed": "no loaded plugins",
            "plugin_version_label": "Version",
            "plugin_id_label": "ID",
            "plugin_author_label": "Author",
            "plugin_permissions_label": "Permissions",
            "plugin_requirements_label": "Requirements",
            "plugin_actions_title": "<b>Actions:</b>",
            "plugin_delete_btn": "🗑 remove",
            "plugin_deleted_alert": "🗑 {name} removed",
            "oa_chat_choice_title": "💬 <b>select target session</b>",
            "remember_pref_continue": "💾 --always-continue",
            "remember_pref_new": "💾 --always-new",
            "pref_saved": "pref written",
        },
    }
    PROVIDERS = (
        "openai",
        "google",
        "openrouter",
        "groq",
        "deepseek",
        "xai",
        "other",
    )
    PROVIDER_LABELS = {
        "openai": "OpenAI",
        "google": "Google",
        "openrouter": "OpenRouter",
        "groq": "Groq",
        "deepseek": "DeepSeek",
        "xai": "xAI",
        "other": "Other",
    }
    DEFAULT_MODELS = {
        "openai": "gpt-5.5",
        "google": "gemini-1.5-flash",
        "openrouter": "openai/gpt-4o-mini",
        "groq": "llama-3.3-70b-versatile",
        "deepseek": "deepseek-chat",
        "xai": "grok-2-latest",
        "other": "gpt-4o-mini",
    }
    BASE_URLS = {
        "openai": "https://api.openai.com/v1",
        "google": "https://generativelanguage.googleapis.com/v1beta",
        "openrouter": "https://openrouter.ai/api/v1",
        "groq": "https://api.groq.com/openai/v1",
        "deepseek": "https://api.deepseek.com/v1",
        "xai": "https://api.x.ai/v1",
    }
    PLACEHOLDER_KEYS = (
        "{agent_version}, {provider}, {provider_key}, {model}, {reasoning_effort}, "
        "{chat_id}, {user_id}, {session_name}, {session_messages}, "
        "{runtime_comments_count}, {runtime_comments}, {tool_count}, {available_tool_count}, "
        "{elapsed}, {input_tokens}, {output_tokens}, {total_tokens}, {thinking}, "
        "{todo}, {random}, {prefix}, {time}, {date}"
    )
    WEB_SEARCH_RE = re.compile(
        r"<web_search>\s*(.*?)\s*</web_search>", re.DOTALL | re.I
    )
    SEND_RE = re.compile(
        r'<send_message(?:\s+chat=["\']([^"\']+)["\'])?\s*>(.*?)</send_message>',
        re.DOTALL | re.I,
    )
    SKILL_RE = re.compile(
        r'<skill\s+name=["\']([^"\']+)["\']\s*>(.*?)</skill>', re.DOTALL | re.I
    )
    CREATE_CHANNEL_RE = re.compile(
        r"<create_channel([^>]*)>(.*?)</create_channel>", re.DOTALL | re.I
    )
    CREATE_GROUP_RE = re.compile(
        r"<create_group([^>]*)>(.*?)</create_group>", re.DOTALL | re.I
    )
    CREATE_BOT_RE = re.compile(
        r"<create_bot([^>]*)>(.*?)</create_bot>", re.DOTALL | re.I
    )
    SEARCH_MESSAGES_RE = re.compile(
        r"<search_messages([^>]*)>(.*?)</search_messages>", re.DOTALL | re.I
    )
    UPDATE_PROFILE_RE = re.compile(
        r"<update_profile([^>]*)>(.*?)</update_profile>", re.DOTALL | re.I
    )
    SET_PROFILE_PHOTO_RE = re.compile(
        r"<set_profile_photo([^>]*)>(.*?)</set_profile_photo>", re.DOTALL | re.I
    )
    DELETE_MESSAGES_RE = re.compile(
        r"<delete_messages([^>]*)>(.*?)</delete_messages>", re.DOTALL | re.I
    )
    FORWARD_MESSAGE_RE = re.compile(
        r"<forward_message([^>]*)>(.*?)</forward_message>", re.DOTALL | re.I
    )
    DOWNLOAD_MEDIA_RE = re.compile(
        r"<download_media([^>]*)>(.*?)</download_media>", re.DOTALL | re.I
    )
    GENERATED_FILE_RE = re.compile(
        r'<file\s+name=["\']([^"\']+)["\']\s*>(.*?)</file>',
        re.DOTALL | re.I,
    )
    MCUB_DOCS_URL = "https://x0.at/y2rb.md"
    TOOL_CALL_RE = re.compile(
        r"<([a-z0-9._]+)([^>]*)>(.*?)</\1>|<([a-z0-9._]+)([^>]*)/?>", re.DOTALL | re.I
    )
    TOOL_CALL_JSON_RE = re.compile(r"```tool_call\s*(.*?)```", re.DOTALL | re.I)
    TOOL_REGISTRY = ()
    # Built-in tools are now discovered dynamically from
    # OpenAgentLib/SystemPlugins/<group>/<tool>.py.
    AGENT_MAX_STEPS = 15
    PREMIUM_EMOJIS = {
        "claude": '<tg-emoji emoji-id="5368808376694248152">💬</tg-emoji>',
        "start": '<tg-emoji emoji-id="5368434680179758177">🏁</tg-emoji>',
        "workout": '<tg-emoji emoji-id="5368387680352637360">🏋️‍♂️</tg-emoji>',
        "party": '<tg-emoji emoji-id="5368635272332352173">🎉</tg-emoji>',
        "loading_dots": '<tg-emoji emoji-id="5328311576736833844">🔴</tg-emoji>',
        "loading_wait": '<tg-emoji emoji-id="5326015457155620929">😐</tg-emoji>',
        "reconnect": '<tg-emoji emoji-id="5325872701032635449">⏳</tg-emoji>',
        "loading_squares": '<tg-emoji emoji-id="5334960765931626355">🎲</tg-emoji>',
        "loading_lava": '<tg-emoji emoji-id="5310041868191407556">🩸</tg-emoji>',
        "soon": '<tg-emoji emoji-id="5411382892850871522">🔜</tg-emoji>',
        "top": '<tg-emoji emoji-id="5411132595041765682">🔝</tg-emoji>',
        "linux": '<tg-emoji emoji-id="5300957668762987048">👩‍💻</tg-emoji>',
        "js": '<tg-emoji emoji-id="5300896259320586992">👩‍💻</tg-emoji>',
        "ts": '<tg-emoji emoji-id="5301254000031572585">👩‍💻</tg-emoji>',
        "grid": '<tg-emoji emoji-id="5294096239464295059">🔵</tg-emoji>',
        "done": '<tg-emoji emoji-id="4916036072560919511">✅</tg-emoji>',
        "warn": '<tg-emoji emoji-id="4915853119839011973">⚠️</tg-emoji>',
        "link": '<tg-emoji emoji-id="4916086774649848789">🔗</tg-emoji>',
        "web": '<tg-emoji emoji-id="4906943755644306322">🌐</tg-emoji>',
        "telegram": '<tg-emoji emoji-id="4918203446202467778">💙</tg-emoji>',
        "at": '<tg-emoji emoji-id="5082413149873767213">💙</tg-emoji>',
        "lock": '<tg-emoji emoji-id="4904500559203009298">🔒</tg-emoji>',
        "bubble": '<tg-emoji emoji-id="4918408122868958076">🖱️</tg-emoji>',
        "back": '<tg-emoji emoji-id="5352759161945867747">🔙</tg-emoji>',
        "block": '<tg-emoji emoji-id="5408830797513784663">🚫</tg-emoji>',
        "blink": '<tg-emoji emoji-id="5411528341918356895">⚪️</tg-emoji>',
        "terminal": '<tg-emoji emoji-id="5409076727341154520">⚙️</tg-emoji>',
        "num_0": '<tg-emoji emoji-id="5140999334174655345">0️⃣</tg-emoji>',
        "num_1": '<tg-emoji emoji-id="5141109049114232089">1️⃣</tg-emoji>',
        "num_2": '<tg-emoji emoji-id="5140871649091912628">2️⃣</tg-emoji>',
        "num_3": '<tg-emoji emoji-id="5141399818400170896">3️⃣</tg-emoji>',
        "num_4": '<tg-emoji emoji-id="5138822752123225428">4️⃣</tg-emoji>',
        "num_5": '<tg-emoji emoji-id="5141062672057369534">5️⃣</tg-emoji>',
        "num_6": '<tg-emoji emoji-id="5139005588881015916">6️⃣</tg-emoji>',
        "num_7": '<tg-emoji emoji-id="5140999557512954818">7️⃣</tg-emoji>',
        "num_8": '<tg-emoji emoji-id="5141013683660391172">8️⃣</tg-emoji>',
        "num_9": '<tg-emoji emoji-id="5141137309999039199">9️⃣</tg-emoji>',
    }
    config = ModuleConfig(
        Group(
            "Provider & Model 🧠",
            [
                ConfigValue(
                    "provider",
                    "openai",
                    description="Provider: openai, google, openrouter, groq, deepseek, xai, other",
                    validator=Choice(choices=list(PROVIDERS)),
                ),
                ConfigValue(
                    "api_key",
                    "",
                    description="API key for the selected provider",
                    validator=Secret(),
                ),
                ConfigValue(
                    "model",
                    "",
                    description="Model name. Empty means provider default",
                    validator=String(),
                ),
                ConfigValue(
                    "custom_base_url",
                    "",
                    description="Endpoint for provider=other, e.g. https://api.deepseek.com/v1",
                    validator=String(),
                ),
                ConfigValue(
                    "system_prompt",
                    "You are OpenAgent inside a Telegram userbot. Help the user directly. You may inspect the local workspace through terminal commands when needed.",
                    description="System prompt for the agent",
                    validator=String(),
                ),
                ConfigValue(
                    "temperature",
                    0.7,
                    description="Sampling temperature",
                    validator=Float(min=0.0, max=2.0),
                ),
                ConfigValue(
                    "max_tokens",
                    1200,
                    description="Maximum response tokens",
                    validator=Integer(min=64, max=32768),
                ),
                ConfigValue(
                    "reasoning_effort",
                    "off",
                    description="Reasoning effort for models/providers that support it: off, low, medium, high, xhigh",
                    validator=Choice(
                        choices=["off", "low", "medium", "high", "xhigh"]
                    ),
                ),
                ConfigValue(
                    "timeout",
                    180,
                    description="HTTP timeout seconds for each provider request. Increase for slow reasoning/code tasks.",
                    validator=Integer(min=10, max=600),
                ),
                ConfigValue(
                    "provider_reconnect_attempts",
                    5,
                    description="Maximum reconnect attempts after provider API timeout",
                    validator=Integer(min=0, max=5),
                ),
            ],
            description="AI provider, credentials, model and request limits",
            button_text="🧠 Provider",
            key="provider_model",
        ),
        Group(
            "Tools & Permissions 🛠",
            [
                ConfigValue(
                    "terminal_enabled",
                    True,
                    description="Allow the agent to execute terminal commands",
                    validator=Boolean(),
                ),
                ConfigValue(
                    "terminal_steps",
                    3,
                    description="Maximum terminal commands per request",
                    validator=Integer(min=0, max=10),
                ),
                ConfigValue(
                    "terminal_timeout",
                    30,
                    description="Terminal command timeout seconds",
                    validator=Integer(min=3, max=120),
                ),
                ConfigValue(
                    "web_search_enabled",
                    True,
                    description="Allow the agent to search the web",
                    validator=Boolean(),
                ),
                ConfigValue(
                    "web_search_steps",
                    3,
                    description="Maximum web searches per request",
                    validator=Integer(min=0, max=10),
                ),
                ConfigValue(
                    "mcub_use",
                    False,
                    description="Allow the agent to execute MCUB userbot commands",
                    validator=Boolean(),
                ),
                ConfigValue(
                    "mcub_steps",
                    3,
                    description="Maximum MCUB commands per request",
                    validator=Integer(min=0, max=10),
                ),
                ConfigValue(
                    "send_messages_enabled",
                    True,
                    description="Allow the agent to send messages as the userbot",
                    validator=Boolean(),
                ),
                ConfigValue(
                    "send_message_steps",
                    3,
                    description="Maximum userbot messages sent per request",
                    validator=Integer(min=0, max=10),
                ),
                ConfigValue(
                    "create_chats_enabled",
                    True,
                    description="Allow the agent to create channels/groups",
                    validator=Boolean(),
                ),
                ConfigValue(
                    "create_chat_steps",
                    2,
                    description="Maximum channels/groups created per request",
                    validator=Integer(min=0, max=5),
                ),
                ConfigValue(
                    "create_bots_enabled",
                    True,
                    description="Allow the agent to create Telegram bots via BotFather",
                    validator=Boolean(),
                ),
                ConfigValue(
                    "create_bot_steps",
                    1,
                    description="Maximum Telegram bots created per request",
                    validator=Integer(min=0, max=3),
                ),
                ConfigValue(
                    "account_tools_enabled",
                    True,
                    description="Allow the agent to edit profile/join chats/read/search messages",
                    validator=Boolean(),
                ),
                ConfigValue(
                    "account_tool_steps",
                    5,
                    description="Maximum account-level tools per request",
                    validator=Integer(min=0, max=15),
                ),
                ConfigValue(
                    "chat_management_enabled",
                    True,
                    description="Allow the agent to manage chats: mute, ban, promote, title, slowmode",
                    validator=Boolean(),
                ),
                ConfigValue(
                    "chat_management_steps",
                    5,
                    description="Maximum chat-management tools per request",
                    validator=Integer(min=0, max=15),
                ),
                ConfigValue(
                    "media_max_bytes",
                    8_000_000,
                    description="Maximum replied media bytes sent to AI",
                    validator=Integer(min=1024, max=25_000_000),
                ),
            ],
            description="Terminal, web, MCUB and Telegram action limits",
            button_text="🛠 Tools",
            key="tools_permissions",
        ),
        Group(
            "Context & Memory 🧾",
            [
                ConfigValue(
                    "context_enabled",
                    True,
                    description="Remember chat context between .oa requests",
                    validator=Boolean(),
                ),
                ConfigValue(
                    "context_turns",
                    10,
                    description="How many user/assistant turns to remember per chat",
                    validator=Integer(min=0, max=50),
                ),
                ConfigValue(
                    "context_compaction_enabled",
                    True,
                    description="Automatically summarize old chat context when it becomes too large",
                    validator=Boolean(),
                ),
                ConfigValue(
                    "context_compaction_chars",
                    18000,
                    description="Compact remembered chat context after this many characters",
                    validator=Integer(min=2000, max=200000),
                ),
                ConfigValue(
                    "context_compaction_keep_turns",
                    2,
                    description="Recent user/assistant turns to keep verbatim after compaction",
                    validator=Integer(min=0, max=10),
                ),
                ConfigValue(
                    "context_compaction_max_tokens",
                    900,
                    description="Maximum tokens used for the compaction summary response",
                    validator=Integer(min=128, max=4096),
                ),
                ConfigValue(
                    "tool_memory_enabled",
                    False,
                    description="Remember concise notes from tool outputs for next requests",
                    validator=Boolean(),
                ),
                ConfigValue(
                    "tool_memory_items",
                    20,
                    description="Maximum remembered tool notes per chat",
                    validator=Integer(min=1, max=200),
                ),
                ConfigValue(
                    "tool_memory_max_chars",
                    500,
                    description="Maximum characters per remembered tool note",
                    validator=Integer(min=80, max=4000),
                ),
            ],
            description="Chat memory, compaction and tool notes",
            button_text="🧾 Context",
            key="context_memory",
        ),
        Row(),
        Group(
            "Templates & Display 🎨",
            [
                ConfigValue(
                    "response_header",
                    '<blockquote><a href="tg://emoji?id=6010179991944305029">☺️</a> <strong>OpenAgent</strong>: <a href="tg://emoji?id=5325872701032635449">⏳</a>  <em>{elapsed}</em>s\n• <u>{provider}/{model}</u>  •  <code>{reasoning_effort}</code>\n| | | | | | | | | | | | | | | | | | | | | | | | | | |\n<a href="tg://emoji?id=5408994848084624514">💸</a> <strong>in</strong> <em>{input_tokens}</em>, <strong>out</strong> <em>{output_tokens}</em> | <b>total</b>\n<i>{total_tokens}</i> | <strong>tool use:</strong> <em>{tool_count}</em></blockquote>\n<blockquote expandable><i>{thinking}</i></blockquote>',
                    description="Final response header template. Placeholders: "
                    + PLACEHOLDER_KEYS,
                    validator=String(),
                ),
                ConfigValue(
                    "request_label",
                    '<a href="tg://emoji?id=6010352868672936598"><strong>🐈‍⬛</strong></a><strong></strong><strong> Prompt:</strong>',
                    description="Request block label template. Placeholders: "
                    + PLACEHOLDER_KEYS,
                    validator=String(),
                ),
                ConfigValue(
                    "response_label",
                    '<a href="tg://emoji?id=6010286885090368072"><strong>❌</strong></a><strong></strong><strong> Answer:</strong>',
                    description="Response block label template. Placeholders: "
                    + PLACEHOLDER_KEYS,
                    validator=String(),
                ),
                ConfigValue(
                    "thinking_template",
                    '<blockquote><a href="tg://emoji?id=6010292571627069263">😎</a> <u>{provider}/{model}</u> • <em>prepares the response...</em></blockquote >\n<blockquote><a href="tg://emoji?id=5404857686477015710">🔄</a><strong><em> {random}</em></strong><em></em></blockquote>',
                    description="Initial loading/thinking message template. Placeholders: "
                    + PLACEHOLDER_KEYS,
                    validator=String(),
                ),
                ConfigValue(
                    "tool_display_template",
                    '<blockquote expandable><i>{thinking_line}</i></blockquote>\n<blockquote expandable><strong>┌|</strong> {tool_state_emoji_html} {status_emoji_html} <em>{status_text}</em> <code>{tool}</code>\n<strong>└|</strong> <a href="tg://emoji?id=6010570945637392851">🥳</a>  <b>Round:</b> <code>{round}/{round_total}</code> • <b>Reasoning:</b>\n<code>{reasoning_effort}</code>\n</blockquote><blockquote><a href="tg://emoji?id=5310041868191407556">🩸</a> <strong>{activity_line}</strong></blockquote>\n<blockquote expandable><a href="tg://emoji?id=6012361831035705571">😪</a> <strong>Log tools</strong>\n<code>{log_lines}</code></blockquote>',
                    description="Tool execution status template. Raw: {tool}, {title}, {value}, {log}, {step}. Semantic: {round}, {round_total}, {progress_bar}, {progress_percent}, {status_emoji}, {status_icon}, {status_emoji_html}, {status_icon_html}, {status_text}, {tool_state}, {tool_state_emoji}, {tool_state_icon}, {tool_state_emoji_html}, {tool_state_icon_html}, {tool_running_emoji}, {tool_running_icon}, {tool_running_emoji_html}, {tool_running_icon_html}, {tool_done_emoji}, {tool_done_icon}, {tool_done_emoji_html}, {tool_done_icon_html}, {tool_group}, {tool_short}, {tool_input}, {tool_input_block}, {thinking_line}, {thinking_block}, {log_lines}, {log_block}, {log_count}, {elapsed_line}, {token_line}, {model_line}, {activity_line}. General placeholders: "
                    + PLACEHOLDER_KEYS,
                    validator=String(),
                ),
                ConfigValue(
                    "tool_status_emojis",
                    "thinking=❔\nterminal=🖥\nweb=🌐\nfile=📦\nmcub=🧲\nmessage=💬\ndialog=🗂\nchat=🐈‍⬛\nmoderation=🛡\nprofile=👤\ncontacts=👥\ncreation=✨\nskills=🧠\ncode=🧬\ncontext=🧾\nutility=🛠\ndefault=🛠",
                    description="Custom emoji/icon map for {status_emoji}/{status_icon}. Format: group_or_tool=emoji per line. Tool-specific keys like terminal.run or thinking.note override groups like terminal/thinking. Premium emoji HTML is allowed via {status_emoji_html}/{status_icon_html}.",
                    validator=String(),
                ),
                ConfigValue(
                    "tool_display_max_chars",
                    1200,
                    description="Maximum chars from current tool input shown in status form",
                    validator=Integer(min=0, max=4000),
                ),
                ConfigValue(
                    "tool_trace_inline_max_chars",
                    6000,
                    description="Maximum chars of a tool call kept inline before the full output is saved to openagent_tool_outputs and replaced by a file path plus preview",
                    validator=Integer(min=0, max=50000),
                ),
                ConfigValue(
                    "tool_display_log_lines",
                    8,
                    description="How many recent tool names to show in status form",
                    validator=Integer(min=0, max=30),
                ),
                ConfigValue(
                    "thinking_display_limit",
                    3,
                    description="How many recent thinking.note entries to show in {thinking}",
                    validator=Integer(min=0, max=20),
                ),
                ConfigValue(
                    "thinking_empty_text",
                    "Модель ещё не думала.",
                    description="Text for {thinking} when no thinking.note entries exist",
                    validator=String(),
                ),
                ConfigValue(
                    "thinking_bullet",
                    "•",
                    description="Prefix marker for each thinking.note line in {thinking}. Empty disables the marker",
                    validator=String(),
                ),
                ConfigValue(
                    "random_strings",
                    ["Thinking...", "Думаю...", "Генерирую..."],
                    description="Random lines for {random}",
                    validator=List(
                        item_type=str,
                    ),
                ),
                ConfigValue(
                    "todo_status_emojis",
                    "pending=...\nopen=>>>\nclosed=---",
                    description="State markers for {todo}. Format: pending=..., open=>>>, closed=---",
                    validator=String(),
                ),
                ConfigValue(
                    "placeholders",
                    "",
                    description="Available OpenAgent placeholders (auto-generated)",
                    validator=String(),
                ),
            ],
            description="Response headers, labels, thinking and tool status templates",
            button_text="🎨 Display",
            key="templates_display",
        ),
        Group(
            "Repo Context & Skills 📚",
            [
                ConfigValue(
                    "repo_context_enabled",
                    True,
                    description="Inject local workspace snapshot into system prompt",
                    validator=Boolean(),
                ),
                ConfigValue(
                    "repo_context_max_chars",
                    7000,
                    description="Maximum chars used for repo context in system prompt",
                    validator=Integer(min=500, max=30000),
                ),
                ConfigValue(
                    "skills_enabled",
                    True,
                    description="Enable loading OpenAgent skills into the system prompt",
                    validator=Boolean(),
                ),
                ConfigValue(
                    "skills_trigger_mode",
                    "auto",
                    description="When to load skills: auto = only on keyword match, always = every request, off = never",
                    validator=String(),
                ),
                ConfigValue(
                    "skill_repo_url",
                    "https://raw.githubusercontent.com/hairpin01/repo-MCUB-fork/main/OpenAgent/skills",
                    description="Base URL for installable OpenAgent skills repository",
                    validator=String(),
                ),
            ],
            description="Workspace context and OpenAgent skills loading",
            button_text="📚 Skills",
            key="repo_skills",
        ),
        Group(
            "Tool Confirmations 🛡",
            [
                ConfigValue(
                    "tool_confirmation_enabled",
                    True,
                    description="Ask for confirmation before tools that can change files, chats, account state, or run commands",
                    validator=Boolean(),
                ),
                ConfigValue(
                    "tool_confirmation_mode",
                    "medium",
                    description="How often to ask before tools: low = only critical/destructive, medium = write/actions, high = almost every non-read tool",
                    validator=Choice(
                        choices=["low", "medium", "high"]
                    ),
                ),
                ConfigValue(
                    "tool_confirmation_template",
                    '<blockquote><a href="tg://emoji?id=6010201728773790293">😈</a> Continue?\n<a href="tg://emoji?id=6012317326584583729">😐</a> Tool: {tool} • {elapsed}s</blockquote>\n<blockquote expandable><a href="tg://emoji?id=6010394680179562842">😶</a> <b>What will be completed</b>\n<a href="tg://emoji?id=6010292550152230657">☀️</a> <code>{value}</code></blockquote>',
                    description="Confirmation form template. Placeholders: {tool}, {value}, {elapsed}, {elapsed_line}",
                    validator=String(),
                ),
                ConfigValue(
                    "tool_confirmation_yes_text",
                    "Выполнить",
                    description="Confirm button text for dangerous tools",
                    validator=String(),
                ),
                ConfigValue(
                    "tool_confirmation_no_text",
                    "Не сейчас",
                    description="Cancel button text for dangerous tools",
                    validator=String(),
                ),
                ConfigValue(
                    "tool_confirmation_timeout",
                    900,
                    description="Seconds to wait for dangerous tool confirmation",
                    validator=Integer(min=10, max=3600),
                ),
            ],
            description="Confirmation policy and prompt/button templates",
            button_text="🛡 Confirm",
            key="confirmations",
        ),
        Row(),
        Answer('❔ About', 'AI agent in userbot with refreshed tool architecture')
    )
    SESSION_LIMIT = 20
    from .MCUBEvent import _MCUBEvent

    @callback(ttl=900)
    async def _open_sessions_panel(
        self, call: InlineMessage, chat_id: int | None = None
    ) -> None:
        cid = int(
            chat_id
            or getattr(call, "chat_id", 0)
            or getattr(call, "_openagent_source_chat_id", 0)
            or 0
        )
        if not cid:
            await call.answer(
                self.strings("error", error="chat_id is missing"), alert=True
            )
            return
        await self._show_sessions_panel(call, cid)

    @callback(ttl=900)
    async def _return_to_last_response(self, call: InlineMessage, chat_id: int) -> None:
        cid = int(chat_id)
        saved_turn = self._last_saved_assistant_turn(cid)
        if not saved_turn:
            await call.answer(self.strings("saved_response_missing"), alert=True)
            return
        prompt, answer, thinking_notes = saved_turn
        with contextlib.suppress(Exception):
            setattr(call, "_openagent_source_chat_id", cid)
        self._set_placeholder_context(call)
        await self._reply_text(
            call,
            answer,
            title=self._response_title(
                0.0, tool_count=0, thinking_notes=thinking_notes
            ),
            prompt=prompt,
            thinking_notes=thinking_notes,
            buttons=self._final_buttons(
                cid,
                prompt,
                prompt,
                [],
                source_event=call,
            ),
            edit_current=True,
        )
        self._store_last_loading(cid, call)

    @callback(ttl=900)
    async def _switch_session(self, call: InlineMessage, session_id: str) -> None:
        session = self._sessions.get(str(session_id))
        if session is None:
            await call.answer(self.strings("skill_not_found"), alert=True)
            return
        self._set_active_session(session.chat_id, session.id)
        self.session_manager.set_preference(session.chat_id, "continue")
        await self._show_sessions_panel(
            call,
            session.chat_id,
            alert=self.strings("chat_switched", name=session.name),
        )

    @callback(ttl=900)
    async def _remember_session_choice(self, call: InlineMessage, chat_id: int) -> None:
        self.session_manager.set_preference(int(chat_id), "continue")
        await self._save_sessions()
        await call.answer(self.strings("chat_choice_saved"), alert=True)

    @callback(ttl=900)
    async def _delete_active_session(self, call: InlineMessage, chat_id: int) -> None:
        cid = int(chat_id)
        sessions = self._get_chat_sessions(cid)
        if len(sessions) <= 1:
            await call.answer(self.strings("chat_delete_last"), alert=True)
            return
        active = self._get_active_session(cid)
        self._sessions.pop(active.id, None)
        remaining = self._get_chat_sessions(cid)
        self._active_session[cid] = remaining[0].id
        await self._save_sessions()
        await self._show_sessions_panel(call, cid, alert=self.strings("chat_deleted"))

    @callback(ttl=900)
    async def _run_pending_here(self, call: InlineMessage, prompt_token: str) -> None:
        """Run pending prompt in the current active session."""
        chat_id = self._pending_prompts.get(prompt_token, {}).get("chat_id")
        if chat_id:
            self.session_manager.set_preference(int(chat_id), "continue")
        await self._execute_pending(call, prompt_token)

    @callback(ttl=900)
    async def _run_pending_in(
        self,
        call: InlineMessage,
        prompt_token: str,
        session_id: str,
    ) -> None:
        """Switch to another session, then run the pending prompt."""
        session = self._sessions.get(str(session_id))
        if session is None:
            with contextlib.suppress(Exception):
                await call.answer(self.strings("chat_delete_last"), alert=True)
            return
        self._set_active_session(session.chat_id, session.id)
        self.session_manager.set_preference(session.chat_id, "continue")
        await self._execute_pending(call, prompt_token)

    @callback(ttl=900)
    async def _remember_pref_continue(
        self,
        call: InlineMessage,
        prompt_token: str,
        chat_id: int,
    ) -> None:
        """Save 'always continue here' pref then run pending in current session."""
        self.session_manager.set_preference(int(chat_id), "continue")
        with contextlib.suppress(Exception):
            await call.answer(self.strings("pref_saved"), alert=False)
        await self._execute_pending(call, prompt_token)

    @callback(ttl=900)
    async def _remember_pref_new(
        self,
        call: InlineMessage,
        prompt_token: str,
        chat_id: int,
    ) -> None:
        """Save 'always create new' pref, create new session, then run."""
        cid = int(chat_id)
        self.session_manager.set_preference(cid, "new")
        self._fresh_session(cid)
        with contextlib.suppress(Exception):
            await call.answer(self.strings("pref_saved"), alert=False)
        await self._execute_pending(call, prompt_token)

    @callback(ttl=900)
    async def _confirm_tool_action(
        self,
        call: InlineMessage,
        token: str | None = None,
        approved: bool = False,
    ) -> None:
        if token:
            future = self._tool_confirmation_waiters.get(token)
            if future is not None and not future.done():
                future.set_result(bool(approved))
        with contextlib.suppress(Exception):
            await call.answer(
                (
                    self.strings("tool_confirmation_approved")
                    if approved
                    else self.strings("cancelled")
                ),
                alert=False,
            )

    @callback(ttl=900)
    async def _activate_inline_status(
        self, call: InlineMessage, token: str | None = None
    ) -> None:
        if token:
            future = self._inline_status_waiters.get(token)
            if future is not None and not future.done():
                future.set_result(call)
        with contextlib.suppress(Exception):
            await call.answer()

    def _oa_arg_parser(self, event: Event) -> Any | None:
        with contextlib.suppress(Exception):
            return self.args(event)
        return None

    def _oa_prompt_from_parser(self, parser: Any | None) -> str:
        if parser is None:
            return ""
        raw = str(getattr(parser, "raw_args", "") or "")
        raw = re.sub(r"(?<!\S)--test(?:=\S+|\s+\S+)?", "", raw)
        raw = re.sub(
            r"(?<!\S)--new(?:=(?:\{[^}]*\}|\"[^\"]*\"|'[^']*'|\S*))?(?=\s|$)", "", raw
        )
        raw = re.sub(r"(?<!\S)(?:--flash|-f)(?=\s|$)", "", raw)
        return re.sub(r"\s+", " ", raw).strip()

    def _oa_flash_arg(self, parser: Any | None) -> bool:
        if parser is None:
            return False
        with contextlib.suppress(Exception):
            if bool(parser.get_flag("flash")) or bool(parser.get_flag("f")):
                return True
        raw = str(getattr(parser, "raw_args", "") or "")
        return bool(re.search(r"(?<!\S)(?:--flash|-f)(?=\s|$)", raw))

    def _oa_new_chat_arg(self, parser: Any | None) -> tuple[bool, str]:
        if parser is None:
            return False, ""
        raw = str(getattr(parser, "raw_args", "") or "")
        match = re.search(
            r"(?<!\S)--new(?:=(?:\{[^}]*\}|\"[^\"]*\"|'[^']*'|\S*))?(?=\s|$)", raw
        )
        if not match:
            return False, ""
        token = match.group(0)
        if "=" not in token:
            return True, ""
        name = token.split("=", 1)[1].strip()
        if len(name) >= 2 and (
            (name[0] == name[-1] and name[0] in {'"', "'"})
            or (name[0] == "{" and name[-1] == "}")
        ):
            name = name[1:-1]
        return True, name.strip()[:64]

    def _oa_test_name(self, parser: Any | None) -> str:
        if parser is None or not hasattr(parser, "get_kwarg"):
            return ""
        return str(parser.get_kwarg("test", "") or "").strip().lower()

    async def _run_oa_test(self, event: Event, name: str) -> None:
        """Run internal OpenAgent smoke tests without hitting real provider APIs."""
        name = (name or "").strip().lower()
        old_once = self._ask_provider_once
        old_show = self._show_agent_action
        old_sleep = asyncio.sleep
        calls: list[int] = []
        statuses: list[str] = []
        log: list[str] = []

        async def no_sleep(_delay: float) -> None:
            return None

        async def fake_show(
            _event: Any,
            title: str,
            value: str,
            _log: list[str],
            tool_name: str = "",
            **_kwargs: Any,
        ) -> None:
            statuses.append(f"{title}:{tool_name}:{value}")

        try:
            asyncio.sleep = no_sleep
            self._show_agent_action = fake_show  # type: ignore[method-assign]
            if name == "reconnect":

                async def fake_once(
                    _provider: str,
                    _messages: list[dict[str, Any]],
                    _api_key: str,
                    *,
                    max_tokens_override: int | None = None,
                ) -> str:
                    calls.append(1)
                    if len(calls) <= 5:
                        raise RuntimeError("Provider request timed out after 1s")
                    return "ok"

                self._ask_provider_once = fake_once  # type: ignore[method-assign]
                result = await self._ask_provider_with_reconnect(
                    "openai",
                    [],
                    "test-key",
                    status_event=event,
                    agent_log=log,
                    started_at=time.monotonic(),
                    thinking_notes=[],
                )
                text = (
                    "Reconnect test OK\n"
                    f"result={result}\n"
                    f"calls={len(calls)}\n"
                    f"statuses={len(statuses)}\n"
                    f"log={', '.join(log)}"
                )
            elif name == "timeout_provider":
                max_reconnects = max(
                    0,
                    min(int(self.config.get("provider_reconnect_attempts", 5) or 0), 5),
                )

                async def fake_once_timeout(
                    _provider: str,
                    _messages: list[dict[str, Any]],
                    _api_key: str,
                    *,
                    max_tokens_override: int | None = None,
                ) -> str:
                    calls.append(1)
                    raise RuntimeError("Provider request timed out after 1s")

                self._ask_provider_once = fake_once_timeout  # type: ignore[method-assign]
                try:
                    await self._ask_provider_with_reconnect(
                        "openai",
                        [],
                        "test-key",
                        status_event=event,
                        agent_log=log,
                        started_at=time.monotonic(),
                        thinking_notes=[],
                    )
                except Exception as exc:
                    text = (
                        "Timeout provider test OK\n"
                        f"max_reconnects={max_reconnects}\n"
                        f"calls={len(calls)}\n"
                        f"statuses={len(statuses)}\n"
                        f"error={type(exc).__name__}: {exc}\n"
                        f"log={', '.join(log)}"
                    )
                else:
                    text = "Timeout provider test FAILED: expected timeout"
            else:
                text = f"Unknown OpenAgent test: {name}"
        finally:
            self._ask_provider_once = old_once  # type: ignore[method-assign]
            self._show_agent_action = old_show  # type: ignore[method-assign]
            asyncio.sleep = old_sleep
        await self.edit(event, html.escape(text), as_html=True)

    def _config_export_blocked_keys(self) -> set[str]:
        return {"api_key", "provider", "model", "custom_base_url"}

    def _exportable_config(self) -> dict[str, Any]:
        blocked = self._config_export_blocked_keys()
        data = self.config.to_dict()
        return {
            key: value
            for key, value in data.items()
            if key not in blocked and value is not None
        }

    async def _read_import_payload(self, event: Event) -> str:
        raw = self._args_raw(event)
        if raw.strip():
            payload = raw.strip()
            if not payload.startswith("{"):
                raise ValueError(
                    "Pass a JSON object after .oaimport or reply to openagent-settings.json"
                )
            return payload
        reply = await event.get_reply_message()
        if not reply:
            return ""
        file_name = getattr(getattr(reply, "file", None), "name", None) or ""
        if file_name.lower().endswith(".json"):
            data = await reply.download_media(file=bytes)
            if data:
                payload = data.decode("utf-8", errors="replace").strip()
                if payload.startswith("{"):
                    return payload
                raise ValueError("Replied .json file does not contain a JSON object")
        text = getattr(reply, "raw_text", None) or getattr(reply, "text", None) or ""
        if text.strip():
            payload = text.strip()
            if payload.startswith("{"):
                return payload
            raise ValueError(
                "Replied message is not OpenAgent settings JSON. Reply to openagent-settings.json or JSON text."
            )
        data = await reply.download_media(file=bytes)
        if data:
            payload = data.decode("utf-8", errors="replace").strip()
            if payload.startswith("{"):
                return payload
            raise ValueError("Replied file does not contain a JSON object")
        return ""

    def _parse_import_config(self, payload: str) -> dict[str, Any]:
        try:
            data = json.loads(payload)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid OpenAgent settings JSON: {exc.msg}") from exc
        if not isinstance(data, dict):
            raise ValueError("JSON object expected")
        settings = data.get("settings", data)
        if not isinstance(settings, dict):
            raise ValueError("settings object expected")
        return settings

    async def _apply_import_config(
        self, settings: dict[str, Any]
    ) -> tuple[list[str], list[str], list[str]]:
        blocked = self._config_export_blocked_keys()
        known = set(self.config.keys())
        applied: list[str] = []
        skipped: list[str] = []
        failed: list[str] = []
        for key, value in settings.items():
            key = str(key)
            if key in blocked or key not in known:
                skipped.append(key)
                continue
            try:
                self.config[key] = value
                applied.append(key)
            except Exception as exc:
                failed.append(f"{key}: {exc}")
        if applied:
            for key in applied:
                self._invalidate_config_caches(key)
            await self.save_config()
        return applied, skipped, failed

    @staticmethod
    def _rich_text_html(text: str, *, limit: int = 30000) -> str:
        text = str(text or "")
        if len(text) > limit:
            text = text[:limit] + "\n… [truncated]"
        escaped = html.escape(text)
        paragraphs = []
        for part in re.split(r"\n{2,}", escaped):
            part = part.strip()
            if part:
                paragraphs.append(f"<p>{part.replace(chr(10), '<br>')}</p>")
        return "".join(paragraphs) or "<p></p>"

    def _rich_bot_system_prompt(self, prompt: str) -> str:
        return (
            self._system_prompt(prompt)
            + "\n\n## Bot command final answer format\n"
            "For this bot command, the final answer is sent as Telegram Rich Message HTML. "
            "Use BlockRich/Rich HTML block formatting directly in the final answer: "
            "<p>, <blockquote>, <pre><code class=\"language-python\">, <details><summary>, "
            "<ul>/<ol>/<li>, <table>/<caption>/<tr>/<th>/<td>, <footer>, <tg-math>, "
            "<tg-math-block>, <tg-emoji>, <tg-reference>, <tg-time>, and media block tags when useful. "
            "Return only the answer body. Do not wrap it in Markdown fences. "
            "The earlier no-XML rule applies only to tool-call syntax; final Rich HTML tags are allowed here."
        )

    @bot_command(
        "oa",
        doc_ru="<запрос> спросить OpenAgent через rich draft streaming",
        doc_en="<prompt> ask OpenAgent using rich draft streaming",
    )
    async def bot_oa(self, event: Event) -> None:
        if event.sender_id != self.kernel.ADMIN_ID:
            return None

        prompt = self.args_raw(event).strip()
        if not prompt:
            await event.reply("Usage: oa <prompt>")
            return

        bot = self.subinline.bot
        if bot is None or not hasattr(bot, "send_draft_message"):
            await event.reply("Rich draft bot client is unavailable")
            return

        target = getattr(event, "chat_id", None) or getattr(event, "sender_id", None)
        if target is None:
            await event.reply("Can't resolve target chat for rich draft")
            return

        draft_id = int.from_bytes(uuid.uuid4().bytes[:8], "big", signed=True)
        started = time.monotonic()

        async def push_draft(label: str) -> None:
            safe_label = html.escape(label)
            with contextlib.suppress(Exception):
                await bot.send_draft_message(
                    target,
                    html=f"<tg-thinking>{safe_label}</tg-thinking>",
                    draft_id=draft_id,
                    noautolink=True,
                )

        await push_draft("OpenAgent думает…")
        task = asyncio.create_task(
            self._ask_agent(
                prompt,
                status_event=None,
                source_event=event,
                attachments=[],
                started_at=started,
                system_override=self._rich_bot_system_prompt(prompt),
            )
        )

        tick = 0
        try:
            while not task.done():
                await asyncio.sleep(1.5)
                tick += 1
                elapsed = time.monotonic() - started
                await push_draft(f"OpenAgent генерирует ответ… {elapsed:.1f}s")

            answer, agent_log, thinking_notes, tool_trace = await task
            elapsed = time.monotonic() - started
            self._remember_context(
                getattr(event, "chat_id", None),
                prompt,
                answer,
                tool_trace,
                thinking_notes,
            )
            final_html = answer.strip() if answer.strip() else "<p></p>"
            if "<" not in final_html or ">" not in final_html:
                final_html = self._rich_text_html(final_html)
            await bot.send_rich_message(
                target,
                html=final_html,
                message=answer[:4096] if answer else "",
            )
        except Exception as exc:
            await push_draft("OpenAgent словил ошибку")
            error_html = (
                "<p><b>OpenAgent error</b></p>"
                f"<blockquote><code>{html.escape(str(exc))}</code></blockquote>"
            )
            with contextlib.suppress(Exception):
                if bot is not None and hasattr(bot, "send_rich_message"):
                    await bot.send_rich_message(target, html=error_html, fallback=True)
                    return
            await event.reply(f"OpenAgent error: {exc}")

    @command(
        "oa",
        alias=["agent"],
        doc_ru="<запрос> спросить ИИ агента; --flash/-f быстрый режим; --new[=имя] новый чат; --chats меню; --clear очистить",
        doc_en="<prompt> ask AI agent; --flash/-f fast mode; --new[=name] new chat; --chats menu; --clear clear",
    )
    async def cmd_oa(self, event: Event) -> None:
        parser = self._oa_arg_parser(event)
        prompt = (
            self._oa_prompt_from_parser(parser)
            if parser is not None
            else self._args_raw(event)
        )
        new_chat, new_chat_name = self._oa_new_chat_arg(parser)
        test_name = self._oa_test_name(parser)
        flash_mode = self._oa_flash_arg(parser)
        if test_name:
            await self._run_oa_test(event, test_name)
            return
        if prompt.strip() == "--clear" or (
            parser is not None and parser.get_flag("clear")
        ):
            chat_id = getattr(event, "chat_id", None)
            if chat_id is not None:
                session = self._get_active_session(int(chat_id))
                session.messages.clear()
                self._tool_memory.pop(int(chat_id), None)
                self._touch_session(session)
                await self.edit(
                    event, html.escape(self.strings("context_cleared")), as_html=True
                )
            else:
                await self.edit(event, self.strings("need_text"))
            return
        if prompt.strip() == "--chats" or (
            parser is not None and parser.get_flag("chats")
        ):
            chat_id = getattr(event, "chat_id", None)
            if chat_id is not None:
                await self._show_sessions_panel(event, int(chat_id), force_inline=True)
            else:
                await self.edit(event, self.strings("need_text"))
            return
        reply_context, attachments = await self._reply_context(event)
        if not prompt and reply_context:
            prompt = self.strings("reply_analyze_prompt")
        if not prompt:
            chat_id = getattr(event, "chat_id", None)
            if chat_id is not None:
                if new_chat:
                    session = self._new_session(
                        int(chat_id), name=new_chat_name or None
                    )
                    self.session_manager.set_preference(int(chat_id), "continue")
                    await self._show_sessions_panel(
                        event,
                        int(chat_id),
                        force_inline=True,
                        alert=self.strings("chat_created", name=session.name),
                    )
                    return
                await self._show_sessions_panel(event, int(chat_id), force_inline=True)
            else:
                await self.edit(event, self.strings("need_text"))
            return

        full_prompt = prompt
        if reply_context:
            full_prompt += f"\n\nReply context:\n{reply_context}"

        chat_id = getattr(event, "chat_id", None)
        if chat_id is not None:
            if new_chat:
                self._new_session(int(chat_id), name=new_chat_name or None)
                self.session_manager.set_preference(int(chat_id), "continue")
            else:
                pref = self._session_prefs.get(int(chat_id), "ask")
                sessions = self._get_chat_sessions(int(chat_id))
                if pref == "new":
                    self._fresh_session(int(chat_id))
                elif pref == "ask" and len(sessions) > 1:
                    prompt_token = self._store_pending_prompt(
                        int(chat_id),
                        prompt,
                        full_prompt,
                        attachments,
                        source_event=event,
                    )
                    await self._show_oa_choice_panel(event, int(chat_id), prompt_token)
                    return

        cancel_token = str(uuid.uuid4())
        self._set_placeholder_context(event, cancel_token)
        self.log.debug(
            "OA cmd_oa: chat_id=%s prompt_len=%d reply=%s attachments=%d",
            chat_id,
            len(prompt),
            bool(reply_context),
            len(attachments or []),
        )
        loading = await self._start_inline_status(
            event,
            self._thinking_text(),
            self._runtime_control_buttons(cancel_token, event),
        )
        started = time.monotonic()
        self.log.debug(
            "OA cmd_oa: status_event type=%s has_edit=%s has_status_buttons=%s",
            type(loading).__name__,
            hasattr(loading, "edit"),
            hasattr(loading, "_openagent_status_buttons"),
        )
        try:
            answer, agent_log, thinking_notes, tool_trace = await self._ask_agent(
                full_prompt,
                status_event=loading or event,
                source_event=event,
                attachments=attachments,
                cancel_token=cancel_token,
                started_at=started,
                flash_mode=flash_mode,
            )
            self._last_request_at = time.time()
            elapsed = time.monotonic() - started
            self._remember_context(
                getattr(event, "chat_id", None),
                full_prompt,
                answer,
                tool_trace,
                thinking_notes,
            )
            await self._reply_text(
                loading or event,
                answer,
                title=self._response_title(
                    elapsed,
                    tool_count=len(agent_log),
                    thinking_notes=thinking_notes,
                ),
                prompt=prompt,
                agent_log=agent_log,
                thinking_notes=thinking_notes,
                buttons=self._final_buttons(
                    getattr(event, "chat_id", None),
                    prompt,
                    full_prompt,
                    attachments,
                    source_event=event,
                ),
                edit_current=True,
            )
            self._store_last_loading(getattr(event, "chat_id", None), loading)
            self._cleanup_runtime_run(cancel_token)
        except Exception as exc:
            self._cleanup_runtime_run(cancel_token)
            await self._reply_error_answer(
                loading or event,
                exc,
                prompt=prompt,
                full_prompt=full_prompt,
                attachments=attachments,
                source_event=event,
                chat_id=getattr(event, "chat_id", None),
                started_at=started,
                source="OpenAgent",
            )

    @command(
        "oaexport",
        doc_ru="экспорт настроек OpenAgent без секретов",
        doc_en="export OpenAgent settings without secrets",
    )
    async def cmd_oaexport(self, event: Event) -> None:
        payload = {
            "name": "OpenAgent settings",
            "version": 1,
            "blocked_keys": sorted(self._config_export_blocked_keys()),
            "settings": self._exportable_config(),
        }
        text = json.dumps(payload, ensure_ascii=False, indent=2)
        data = io.BytesIO(text.encode("utf-8"))
        data.name = "openagent-settings.json"
        try:
            await self.client.send_file(
                event.chat_id,
                data,
                caption="OpenAgent settings export (without provider/API secrets)",
            )
            with contextlib.suppress(Exception):
                await event.delete()
        except Exception:
            await self.edit(event, f"<pre>{html.escape(text)}</pre>", as_html=True)

    @command(
        "oaimport",
        doc_ru="импорт настроек OpenAgent без секретов из reply/JSON",
        doc_en="import OpenAgent settings without secrets from reply/JSON",
    )
    async def cmd_oaimport(self, event: Event) -> None:
        try:
            payload = await self._read_import_payload(event)
            if not payload:
                await self.edit(
                    event,
                    "Reply to openagent-settings.json or pass JSON after .oaimport",
                )
                return
            settings = self._parse_import_config(payload)
            applied, skipped, failed = await self._apply_import_config(settings)
        except Exception as exc:
            await self.edit(
                event, self.strings("error", error=html.escape(str(exc))), as_html=True
            )
            return
        lines = [
            "OpenAgent settings import complete",
            f"applied: {len(applied)}",
            f"skipped: {len(skipped)}",
            f"failed: {len(failed)}",
        ]
        if skipped:
            lines.append("skipped keys: " + ", ".join(sorted(skipped)[:30]))
        if failed:
            lines.append("failed keys: " + "; ".join(failed[:10]))
        await self.edit(
            event,
            "<blockquote>" + html.escape("\n".join(lines)) + "</blockquote>",
            as_html=True,
        )

    @command(
        "skills", doc_ru="список скиллов OpenAgent", doc_en="list OpenAgent skills"
    )
    async def cmd_skills(self, event: Event) -> None:
        arg = self._args_raw(event)
        if arg in {"-repo", "--repo", "repo"}:
            try:
                text = await self._format_skill_repo_list()
            except Exception as exc:
                await self.edit(
                    event,
                    html.escape(self.strings("error", error=str(exc))),
                    as_html=True,
                )
                return
            await self.edit(event, "<pre>" + html.escape(text) + "</pre>", as_html=True)
            return

        skills = self._list_skills()
        if not skills:
            await self.edit(event, self.strings("skills_empty"))
            return
        lines = []
        for path in skills:
            try:
                text = path.read_text(encoding="utf-8")
                first_line = text.splitlines()[0] if text.splitlines() else ""
                frontmatter_name = re.search(
                    r"^name:\s*(.+)$", text, flags=re.MULTILINE
                )
                frontmatter_description = re.search(
                    r"^description:\s*(.+)$", text, flags=re.MULTILINE
                )
            except Exception:
                first_line = ""
                frontmatter_name = None
                frontmatter_description = None
            name = (
                frontmatter_name.group(1).strip()
                if frontmatter_name
                else self._skill_name_from_path(path)
            )
            title = (
                frontmatter_description.group(1).strip()
                if frontmatter_description
                else (
                    first_line.lstrip("# ").strip()
                    if first_line.startswith("#")
                    else name
                )
            )
            lines.append(f"- {name}: {title}")
        await self.edit(
            event, "<pre>" + html.escape("\n".join(lines)) + "</pre>", as_html=True
        )

    @command(
        "skillinstall",
        alias=["ssinstall"],
        doc_ru="<name> установить OpenAgent skill из repo",
        doc_en="<name> install OpenAgent skill from repo",
    )
    async def cmd_skillinstall(self, event: Event) -> None:
        name = self._args_raw(event)
        if not name:
            await self.edit(event, self.strings("skillinstall_usage"))
            return
        try:
            saved_name = await self._install_repo_skill(name)
        except Exception as exc:
            await self.edit(
                event, html.escape(self.strings("error", error=str(exc))), as_html=True
            )
            return
        await self.edit(
            event,
            self.strings("skill_installed", name=html.escape(saved_name)),
            as_html=True,
        )

    @command(
        "sendss", doc_ru="<name> отправить .md скилл", doc_en="<name> send skill .md"
    )
    async def cmd_sendss(self, event: Event) -> None:
        name = self._args_raw(event)
        if not name:
            await self.edit(event, self.strings("sendss_usage"))
            return
        path = self._find_skill_path(name)
        if not path.exists():
            await self.edit(event, self.strings("skill_not_found"))
            return
        await self.client.send_file(
            event.chat_id,
            str(path),
            caption=f"<b>Skill:</b> <code>{html.escape(self._skill_name_from_path(path))}</code>",
            parse_mode="html",
        )
        try:
            await event.delete()
        except Exception:
            pass

    @command(
        "imss",
        doc_ru="[name] импортировать .md скилл из reply",
        doc_en="[name] import .md skill from reply",
    )
    async def cmd_imss(self, event: Event) -> None:
        reply = await event.get_reply_message()
        if not reply:
            await self.edit(event, self.strings("imss_need_reply"))
            return

        name = self._args_raw(event)
        file_name = getattr(getattr(reply, "file", None), "name", None) or ""
        content = ""
        try:
            data = await reply.download_media(file=bytes)
            if data:
                content = data.decode("utf-8", errors="replace")
        except Exception:
            content = ""

        if not content:
            content = (
                getattr(reply, "raw_text", None) or getattr(reply, "text", "") or ""
            )
        if not content.strip():
            await self.edit(event, self.strings("skill_empty"))
            return

        if not name:
            if file_name.lower().endswith(".md"):
                name = Path(file_name).stem
            else:
                match = re.search(r"^#\s+(.+)$", content, flags=re.MULTILINE)
                name = match.group(1).strip() if match else "skill"

        saved_name = self._save_skill(name, content)
        await self.edit(
            event,
            self.strings("skill_imported", name=html.escape(saved_name)),
            as_html=True,
        )

    @command("delss", doc_ru="<name> удалить скилл", doc_en="<name> delete skill")
    async def cmd_delss(self, event: Event) -> None:
        name = self._args_raw(event)
        if not name:
            await self.edit(event, self.strings("delss_usage"))
            return
        path = self._find_skill_path(name)
        if not path.exists():
            await self.edit(event, self.strings("skill_not_found"))
            return
        path.unlink()
        try:
            if path.name == "SKILL.md" and not any(path.parent.iterdir()):
                path.parent.rmdir()
        except Exception:
            pass
        await self.edit(
            event,
            self.strings(
                "skill_deleted", name=html.escape(self._skill_name_from_path(path))
            ),
            as_html=True,
        )

    def _format_oaplugin_overview(self) -> str:
        installed = self._plugins
        text = self.strings("plugins_enabled_title")
        if not installed:
            text += self.strings("plugins_none_installed")
        else:
            for pname, plugin in sorted(installed.items()):
                display_name = self._plugin_meta_text(plugin, "name", default=pname)
                version = self._plugin_meta_text(plugin, "version", default="?")
                desc = self._plugin_meta_text(
                    plugin,
                    "description",
                    default=self.strings("plugin_no_description"),
                )
                author = self._plugin_meta_text(plugin, "author")
                tools = self._plugin_tool_names(plugin)[:5]
                item_lines = [
                    f"<b>{html.escape(display_name)}</b> <code>v{html.escape(version)}</code>"
                ]
                if display_name.lower() != str(pname).lower():
                    item_lines.append(
                        f"{html.escape(self.strings('plugin_id_label'))}: "
                        f"<code>{html.escape(str(pname))}</code>"
                    )
                if desc:
                    item_lines.append(html.escape(desc))
                if author:
                    item_lines.append(
                        f"{html.escape(self.strings('plugin_author_label'))}: {html.escape(author)}"
                    )
                if tools:
                    tools_text = ", ".join(
                        f"<code>{html.escape(tool)}</code>" for tool in tools
                    )
                    item_lines.append(
                        f"{html.escape(self.strings('plugin_tools_label'))}: {tools_text}"
                    )
                text += "<blockquote>" + "\n".join(item_lines) + "</blockquote>\n"
        text += self.strings("plugins_total", count=len(installed))
        return text

    @command(
        "oaplugin",
        doc_ru="управление плагинами OpenAgent",
        doc_en="manage OpenAgent plugins",
    )
    async def cmd_oaplugin(self, event: Event) -> None:
        """Show plugin manager or install a plugin from replied .py file."""
        if await event.get_reply_message():
            try:
                saved_name = await self._install_plugin_from_reply(event)
            except Exception as exc:
                await self.edit(
                    event,
                    self.strings("plugin_install_failed", error=html.escape(str(exc))),
                    as_html=True,
                )
                return
            await self.edit(
                event,
                self.strings("plugin_installed", name=html.escape(saved_name)),
                as_html=True,
            )
            return

        text = self._format_oaplugin_overview()

        buttons = [
            [
                self.Button.inline(
                    self.strings("plugin_catalog_btn"),
                    self._oaplugin_catalog,
                    args=(0,),
                    style="primary",
                ),
                self.Button.inline(
                    self.strings("plugin_manager_btn"),
                    self._oaplugin_manager,
                    args=(0,),
                    style="primary",
                ),
            ],
            [
                self.Button.inline(
                    self.strings("close_btn"), self._oaplugin_close, style="danger"
                ),
            ],
        ]

        chat_id = getattr(event, "chat_id", None)
        if chat_id:
            try:
                await self.inline(
                    chat_id,
                    text,
                    buttons=buttons,
                    ttl=900,
                    parse_mode="html",
                    reply_to=getattr(event, "reply_to", None),
                )
                await event.delete()
            except Exception:
                await self.edit(event, text, as_html=True)
        else:
            await self.edit(event, text, as_html=True)

    @callback(ttl=900)
    async def _oaplugin_close(self, call: InlineMessage) -> None:
        try:
            await call.delete()
        except Exception:
            await call.answer()

    @callback(ttl=900)
    async def _oaplugin_catalog(self, call: InlineMessage, page: int = 0) -> None:
        """Show available plugins from repo (xheta-style)."""
        plugins = self._plugins_cache
        if not plugins:
            plugins = await self._fetch_repo_plugins()
        if not plugins:
            await call.answer(self.strings("plugin_repo_empty"), alert=True)
            return
        if page < 0 or page >= len(plugins):
            await call.answer()
            return
        m = plugins[page]
        name = self._doc_text(m.get("name", "?"), default="?")
        author = self._doc_text(m.get("author", "?"), default="?")
        version = self._doc_text(m.get("version", "?"), default="?")
        desc = self._doc_text(
            m.get("description", self.strings("plugin_no_description")),
            default=self.strings("plugin_no_description"),
        )
        tools = self._string_list(m.get("tools", []))
        permissions = self._string_list(m.get("permissions", []))
        requirements = self._string_list(m.get("requirements", []))
        fname = m.get("file_name", "")
        plugin_key = self._safe_plugin_name(
            m.get("plugin_name") or fname.replace(".py", "") or name
        )
        installed = plugin_key in self._plugins

        text = (
            f"📦 <b>{html.escape(name)}</b> "
            f"<code>v{html.escape(version)}</code> "
            f"by <code>{html.escape(author)}</code>\n\n"
        )
        text += f"📝 {html.escape(desc)}\n"
        if tools:
            tools_str = ", ".join(f"<code>{html.escape(t)}</code>" for t in tools[:8])
            if len(tools) > 8:
                tools_str += self.strings("plugin_more_tools", count=len(tools) - 8)
            text += f"\n🔧 <b>{html.escape(self.strings('plugin_tools_label'))}:</b> {tools_str}"
        if permissions:
            perms_str = ", ".join(f"<code>{html.escape(item)}</code>" for item in permissions)
            text += f"\n🔐 <b>{html.escape(self.strings('plugin_permissions_label'))}:</b> {perms_str}"
        if requirements:
            reqs_str = ", ".join(f"<code>{html.escape(item)}</code>" for item in requirements)
            text += f"\n📦 <b>{html.escape(self.strings('plugin_requirements_label'))}:</b> {reqs_str}"
        text += f"\n\n🔢 {page + 1}/{len(plugins)}"

        buttons = []
        raw_url = m.get("download_url", "")
        if installed:
            buttons.append(
                [
                    self.Button.inline(
                        self.strings("plugin_installed_btn"),
                        self._oaplugin_noop,
                        style="primary",
                    )
                ]
            )
        else:
            buttons.append(
                [
                    self.Button.inline(
                        self.strings("plugin_install_btn"),
                        self._oaplugin_install,
                        args=(fname.replace(".py", ""), page),
                        style="primary",
                    )
                ]
            )
        if raw_url:
            buttons[0].append(self.Button.url(self.strings("plugin_code_btn"), raw_url))

        nav = []
        if page > 0:
            nav.append(
                self.Button.inline(
                    "⬅️", self._oaplugin_catalog, args=(page - 1,), style="primary"
                )
            )
        nav.append(
            self.Button.inline(
                f"📋 {page + 1}/{len(plugins)}", self._oaplugin_noop, style="primary"
            )
        )
        if page < len(plugins) - 1:
            nav.append(
                self.Button.inline(
                    "➡️", self._oaplugin_catalog, args=(page + 1,), style="primary"
                )
            )
        if nav:
            buttons.append(nav)
        buttons.append(
            [
                self.Button.inline(
                    self.strings("back_btn"), self._oaplugin_main, style="primary"
                )
            ]
        )

        try:
            await call.edit(text, buttons=buttons, parse_mode="html")
        except Exception:
            pass

    @callback(ttl=900)
    async def _oaplugin_noop(self, call: InlineMessage) -> None:
        await call.answer()

    @callback(ttl=900)
    async def _oaplugin_main(self, call: InlineMessage) -> None:
        """Return to main plugin page."""
        text = self._format_oaplugin_overview()
        buttons = [
            [
                self.Button.inline(
                    self.strings("plugin_catalog_btn"),
                    self._oaplugin_catalog,
                    args=(0,),
                    style="primary",
                ),
                self.Button.inline(
                    self.strings("plugin_manager_btn"),
                    self._oaplugin_manager,
                    args=(0,),
                    style="primary",
                ),
            ],
            [
                self.Button.inline(
                    self.strings("close_btn"), self._oaplugin_close, style="danger"
                ),
            ],
        ]
        try:
            await call.edit(text, buttons=buttons, parse_mode="html")
        except Exception:
            pass

    @callback(ttl=900)
    async def _oaplugin_install(
        self, call: InlineMessage, name: str, page: int = 0
    ) -> None:
        """Download and install a plugin from repo."""
        await call.answer(self.strings("plugin_installing"), alert=False)
        try:
            saved_name = await self._install_plugin_from_repo(name)
            await call.answer(
                self.strings("plugin_installed_alert", name=saved_name), alert=True
            )
        except Exception as exc:
            await call.answer(self.strings("generic_error", error=str(exc)), alert=True)
            return
        plugins = self._plugins_cache
        if plugins and page < len(plugins):
            await self._oaplugin_catalog(call, page)
        else:
            await self._oaplugin_catalog(call, 0)

    @callback(ttl=900)
    async def _oaplugin_manager(self, call: InlineMessage, page: int = 0) -> None:
        """Show installed plugins with delete option."""
        installed = list(self._plugins.items())
        if not installed:
            await call.answer(self.strings("plugin_manager_no_installed"), alert=True)
            return
        if page < 0 or page >= len(installed):
            await call.answer()
            return
        plugin_id, plugin = installed[page]
        plugin_id = str(plugin_id or getattr(plugin, "name", "") or "?")
        display_name = self._plugin_meta_text(plugin, "name", default=plugin_id)
        version = self._plugin_meta_text(plugin, "version", default="?")
        desc = self._plugin_meta_text(plugin, "description", default=self.strings("plugin_no_description"))
        author = self._plugin_meta_text(plugin, "author")
        tools = self._plugin_tool_names(plugin)
        permissions = self._plugin_permissions(plugin)
        requirements = self._plugin_requirements(plugin)

        text = f"<b>⚙️ {html.escape(display_name)}</b>\n"
        if display_name.lower() != plugin_id.lower():
            text += f"{html.escape(self.strings('plugin_id_label'))}: <code>{html.escape(plugin_id)}</code>\n"
        text += f"{html.escape(self.strings('plugin_version_label'))}: <code>{html.escape(version)}</code>\n"
        if author:
            text += f"{html.escape(self.strings('plugin_author_label'))}: {html.escape(author)}\n"
        if desc:
            text += f"\n{html.escape(desc)}\n"
        if tools:
            tools_str = ", ".join(f"<code>{html.escape(tool)}</code>" for tool in tools[:8])
            if len(tools) > 8:
                tools_str += self.strings("plugin_more_tools", count=len(tools) - 8)
            text += f"\n{html.escape(self.strings('plugin_tools_label'))}: {tools_str}\n"
        if permissions:
            perms_str = ", ".join(f"<code>{html.escape(item)}</code>" for item in permissions)
            text += f"{html.escape(self.strings('plugin_permissions_label'))}: {perms_str}\n"
        if requirements:
            reqs_str = ", ".join(f"<code>{html.escape(item)}</code>" for item in requirements)
            text += f"{html.escape(self.strings('plugin_requirements_label'))}: {reqs_str}\n"
        text += "\n"
        text += self.strings("plugin_actions_title")
        row1 = [
            self.Button.inline(
                self.strings("plugin_delete_btn"),
                self._oaplugin_uninstall,
                args=(plugin_id, page),
                style="danger",
            )
        ]
        buttons = [row1]
        if len(installed) > 1:
            nav = []
            if page > 0:
                nav.append(
                    self.Button.inline(
                        "⬅️", self._oaplugin_manager, args=(page - 1,), style="primary"
                    )
                )
            nav.append(
                self.Button.inline(
                    f"{page + 1}/{len(installed)}", self._oaplugin_noop, style="primary"
                )
            )
            if page < len(installed) - 1:
                nav.append(
                    self.Button.inline(
                        "➡️", self._oaplugin_manager, args=(page + 1,), style="primary"
                    )
                )
            buttons.append(nav)
        buttons.append(
            [
                self.Button.inline(
                    self.strings("back_btn"), self._oaplugin_main, style="primary"
                )
            ]
        )
        try:
            await call.edit(text, buttons=buttons, parse_mode="html")
        except Exception:
            pass

    @callback(ttl=900)
    async def _oaplugin_uninstall(
        self, call: InlineMessage, name: str, page: int = 0
    ) -> None:
        """Delete a plugin."""
        try:
            name = self._safe_plugin_name(name)
            fpath = self._plugin_files.get(name)
            is_builtin = bool(fpath and self._is_builtin_plugin_file(fpath))
            if is_builtin:
                self._disabled_plugins.add(name)
                self._save_disabled_plugins()
            self._unregister_plugin(name)
            plugins_dir = self._resolve_plugins_dir()
            if fpath and fpath.exists() and not is_builtin:
                try:
                    fpath.resolve().relative_to(plugins_dir.resolve())
                    fpath.unlink()
                except ValueError:
                    pass
            if not is_builtin:
                for extra in (
                    plugins_dir / f"{name}.py",
                    plugins_dir / f"{name}_plugin.py",
                ):
                    if extra.exists():
                        extra.unlink()
            await call.answer(
                self.strings("plugin_deleted_alert", name=name), alert=True
            )
        except Exception as exc:
            await call.answer(self.strings("generic_error", error=str(exc)), alert=True)
            return
        await self._oaplugin_manager(
            call, min(page, len(self._plugins) - 1) if self._plugins else 0
        )
