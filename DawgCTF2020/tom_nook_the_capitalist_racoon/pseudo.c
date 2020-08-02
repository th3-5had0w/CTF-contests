void sell(void)

{
  int iVar1;
  size_t sVar2;
  int local_18;
  int local_14;
  
  local_18 = 0;
  sVar2 = strlen(sell_str);
  print_string(sell_str,sVar2 & 0xffffffff);
  local_14 = 0;
  while (local_14 < 5) {
    if (*(int *)(valid_items + (long)local_14 * 4) != 0) {
      printf("%d. %s - %s Price: %d bells\n",(ulong)(local_14 + 1),my_items + (long)local_14 * 0x54,
             (long)local_14 * 0x54 + 0x1055b4,
             (ulong)*(uint *)(my_items + (long)local_14 * 0x54 + 0x48));
    }
    local_14 = local_14 + 1;
  }
  scanf("%d",&local_18);
  do {
    iVar1 = getchar();
  } while (iVar1 != 10);
  putchar(10);
  if (((local_18 < 1) || (5 < local_18)) || (*(int *)(valid_items + (long)(local_18 + -1) * 4) == 0)
     ) {
    puts("Invalid Choice");
  }
  else {
    sell_item((ulong)(local_18 - 1));
  }
  return;
}



void store(void)

{
  int iVar1;
  size_t sVar2;
  int local_14;
  
  while( true ) {
    while( true ) {
      local_14 = 0;
      puts("1. I want to sell");
      puts("2. What\'s for sale?");
      puts("3. See you later.");
      printf("Choice: ");
      scanf("%d",&local_14);
      do {
        iVar1 = getchar();
      } while (iVar1 != 10);
      putchar(10);
      if (local_14 != 2) break;
      if (num_items < 5) {
        sale();
      }
      else {
        sVar2 = strlen(bag_full);
        print_string(bag_full,sVar2 & 0xffffffff);
      }
    }
    if (local_14 == 3) break;
    if (local_14 == 1) {
      sell();
    }
  }
  exit_game();
}
