@echo off

rem cd c:\users\janeiros\Desktop\reconcile_open_positions

for %%f in (*.csv) do check_reconcile.py %%f

pause

