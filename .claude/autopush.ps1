$j = [Console]::In.ReadToEnd()
if ($j -match '"command"\s*:\s*"git commit') {
    git -C "C:\Users\smeet\OneDrive\Desktop\Tribal Zone" push 2>$null
}
