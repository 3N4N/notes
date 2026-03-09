command! -nargs=0 PanThis 
      \ silent execute '!pandoc' expand('%')
      \ '-o' expand('%:r') . '.html'
      \ '-s -f markdown+smart --toc --to=html5+smart --template templates/tufte'
      \ '-c ../css/pandoc.css -c ../css/tufte.css -c ../css/tufte-extra.css'
      \ | execute ':redraw!'
nnoremap <Leader>p :PanThis<CR>
