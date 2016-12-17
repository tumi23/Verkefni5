import pygame, pygame.mixer
from bomb import Bomb

def game_loop(screen, background, clock, bombs_list, level, brickWall_list, all_sprite_list, player1, player2, blast_list):

    carryOnMyWaywardSon = True

    while carryOnMyWaywardSon:

        for b in bombs_list:
            if b.time + 3000 < pygame.time.get_ticks():
                blast = b.detonate(level, brickWall_list, all_sprite_list, player1)
                bombs_list.remove(b)
                all_sprite_list.remove(b)
                blast_list.add(blast)
                all_sprite_list.add(blast)

        for bl in blast_list:
            if bl.time + 500 < pygame.time.get_ticks():
                blast_list.remove(bl)
                all_sprite_list.remove(bl)

        blast_collision_list = pygame.sprite.spritecollide(player1, blast_list, False)
        for p in blast_collision_list:
            print(p)
            print("Yo player 1, yu Dead!")
            # End Of Game
            carryOnMyWaywardSon = False
            break
        blast_collision_list = pygame.sprite.spritecollide(player2, blast_list, False)
        for p in blast_collision_list:
            print(p)
            print("Yo player 2, yu  Dead!")
            # End Of Game
            carryOnMyWaywardSon = False
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                # TODO functionize
                if event.key == pygame.K_LEFT:
                    player1.changespeed(-3, 0)
                elif event.key == pygame.K_RIGHT:
                    player1.changespeed(3, 0)
                elif event.key == pygame.K_UP:
                    player1.changespeed(0, -3)
                elif event.key == pygame.K_DOWN:
                    player1.changespeed(0, 3)
                elif event.key == pygame.K_SPACE:
                    bomb = Bomb(player1)
                    all_sprite_list.add(bomb)
                    bombs_list.add(bomb)
                    last_bomb_time = pygame.time.get_ticks()

                elif event.key == pygame.K_a:
                    player2.changespeed(-3, 0)
                elif event.key == pygame.K_d:
                    player2.changespeed(3, 0)
                elif event.key == pygame.K_w:
                    player2.changespeed(0, -3)
                elif event.key == pygame.K_s:
                    player2.changespeed(0, 3)
                elif event.key == pygame.K_q:
                    bomb = Bomb(player2)
                    all_sprite_list.add(bomb)
                    bombs_list.add(bomb)
                    last_bomb_time = pygame.time.get_ticks()

                elif event.key == pygame.K_ESCAPE:
                    carryOnMyWaywardSon = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player1.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    player1.changespeed(-3, 0)
                elif event.key == pygame.K_UP:
                    player1.changespeed(0, 3)
                elif event.key == pygame.K_DOWN:
                    player1.changespeed(0, -3)

                elif event.key == pygame.K_a:
                    player2.changespeed(3, 0)
                elif event.key == pygame.K_d:
                    player2.changespeed(-3, 0)
                elif event.key == pygame.K_w:
                    player2.changespeed(0, 3)
                elif event.key == pygame.K_s:
                    player2.changespeed(0, -3)

        screen.blit(background, (0, 0))
        all_sprite_list.update()

        all_sprite_list.draw(screen)

        pygame.display.flip()

        clock.tick(60)

