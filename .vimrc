filetype indent on
set smartindent
set smarttab
set nu
set expandtab
set tabstop=4
set softtabstop=4
set shiftwidth=4
" 开启语法高亮
syntax on
" 设置文字编码自动识别
set fencs=utf-8,cp936
" 使用鼠标
set mouse=v
" 设置高亮搜索
set hlsearch
" 输入字符串就显示匹配点
set incsearch
" 输入的命令显示出来，看的清楚些。
set showcmd
" Tlist的内部变量。函数列表。
let Tlist_Use_Right_Window=1
let Tlist_File_Fold_Auto_Close=1
" 打开当前目录文件列表
map <F3> :Explore<CR>
" 函数和变量列表
map <F4> :TlistToggle<CR>
" 全能补全
inoremap <F8> <C-x><C-o>
" 没事，鼠标画线玩的。
" noremap <F9> :call ToggleSketch()<CR>
" 启动函数变量快速浏览的时间设置
set updatetime=100
set cindent
map <C-o> :WMToggle<CR>
map <F5> :cnext<CR>
map <F6> :cprev<CR>
map <F7> :call Searchword()<CR>
set tabstop=4
set nocp
filetype plugin on


set tags+=~/.vim/tags/cpp
set tags+=~/.vim/tags/c
set tags+=~/.vim/tags/gl
set tags+=~/.vim/tags/sdl
"set tags+=~/.vim/tags/qt4
set tags+=~/.vim/tags/systags
"build tags of your own  project with Ctrl-F12
map <C-p> :!ctags -R --sort=yes --c++-kinds=+p --fields=+iaS --extra=+q .<CR>


"0mniCppComplete
let OmniCpp_NamespaceSearch = 1
let OmniCpp_GlobalScopeSearch = 1
let OmniCpp_ShowAccess = 1
let OmniCpp_ShowPrototypeInAbbr = 1 " show function parameters
let OmniCpp_MayCompleteDot = 1 " autocomplete after .
let OmniCpp_MayCompleteArrow = 1 " autocomplete after ->
let OmniCpp_MayCompleteScope = 1 " autocomplete after ::
let OmniCpp_DefaultNamespaces = ["std", "_GLIBCXX_STD"]
" automatically open and close the popup menu / preview window
au CursorMovedI,InsertLeave * if pumvisible() == 0|silent! pclose|endif
set completeopt=menuone,menu,longest,preview

"用来设置自动添加注释 Dox  DoxAuthor DoxBlock
let g:DoxygenToolkit_authorName="xwp_fullstack@163.com"
let g:DoxygenToolkit_briefTag_funcName="yes"

map <F9> :Dox<CR>
map <F8> :DoxAuthor<CR>
