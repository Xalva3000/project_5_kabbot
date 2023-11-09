from random import choice
from typing import Iterable

from sqlalchemy import delete, select
from sqlalchemy.sql.expression import func

from database.database import MinBookOrm
from database.database import (KabDictionary, MinFragments, Questionable,
                               UserBookmarksOrm, UsersOrm, UserTextOrm,
                               async_session)
from database.temporary_info import usersdictplaycache

"""Файл для хранения асинхронных запросов"""


class AsyncQuery:
    @staticmethod
    async def insert_user(u_id: int, name: str):
        async with async_session() as session:
            if isinstance(u_id, int) and isinstance(name, str | None):
                session.add(UsersOrm(user_id=u_id, name=name))
                await session.commit()
            else:
                return "wrong data types"

    @staticmethod
    async def select_user(u_id: int):
        async with async_session() as session:
            result = await session.get(UsersOrm, u_id)
            return result

    @staticmethod
    async def select_user_book_page(u_id: int):
        async with async_session() as session:
            result = await session.get(UsersOrm, u_id)
            return result.current_mn_page

    @staticmethod
    async def update_users_book_page(u_id: int, new_page: str | int = "forward"):
        async with async_session() as session:
            user = await session.get(UsersOrm, u_id)
            if new_page == "forward":
                user.current_mn_page += 1
            elif new_page == "backward" and user.current_mn_page > 0:
                user.current_mn_page -= 1
            elif isinstance(new_page, int) and new_page >= 0:
                user.current_mn_page = new_page
            await session.commit()

    @staticmethod
    async def update_users_kabdict_page(u_id, new_page: str | int = "forward"):
        async with async_session() as session:
            user = await session.get(UsersOrm, u_id)
            if new_page == "forward":
                user.current_dict_page += 1
            elif new_page == "backward" and user.current_dict_page > 1:
                user.current_dict_page -= 1
            elif isinstance(new_page, int) and new_page > 0:
                user.current_dict_page = new_page
            await session.commit()

    @staticmethod
    async def update_users_wrong_answer(u_id):
        async with async_session() as session:
            user = await session.get(UsersOrm, u_id)
            user.answers += 1
            user.wrong_answers += 1
            await session.commit()

    @staticmethod
    async def update_users_right_answer(u_id):
        async with async_session() as session:
            user = await session.get(UsersOrm, u_id)
            user.answers += 1
            user.right_answers += 1
            await session.commit()

    @staticmethod
    async def reset_users_stats(u_id):
        async with async_session() as session:
            user = await session.get(UsersOrm, u_id)
            user.answers = 0
            user.right_answers = 0
            user.wrong_answers = 0
            await session.commit()

    @staticmethod
    async def insert_book_pages(book: dict[int:tuple]):
        async with async_session() as session:
            for key, tpl in book.items():
                session.add(
                    MinBookOrm(page_id=key, fragment_id=tpl[0], page_text=tpl[1])
                )
            await session.commit()

    @staticmethod
    async def select_book_page(page: int | Iterable):
        async with async_session() as session:
            if isinstance(page, int):
                result = await session.get(MinBookOrm, page)
                return result.page_text, result.fragment_id
            else:
                stmt = (
                    select(MinBookOrm)
                    .where(MinBookOrm.page_id.in_(set(page)))
                    .limit(10)
                )
                result = await session.execute(stmt)
                return result.scalars().fetchall()

    # запрос максимального номера страницы для клавиатуры пагинации книги
    @staticmethod
    async def select_max_book_page() -> int:
        async with async_session() as session:
            stmt = select(func.max(MinBookOrm.page_id))
            result = await session.execute(stmt)
            return result.scalars().one()

    @staticmethod
    async def insert_bookmark(user_id, page):
        async with async_session() as session:
            session.add(UserBookmarksOrm(user_id=user_id, page=page))
            await session.commit()

    @staticmethod
    async def select_users_bookmarks(user_id):
        async with async_session() as session:
            stmt = select(UserBookmarksOrm).filter_by(user_id=user_id)
            result = await session.execute(stmt)
            return result.scalars().fetchall()

    @staticmethod
    async def delete_users_bookmark(user_id, page):
        async with async_session() as session:
            stmt = delete(UserBookmarksOrm).filter_by(user_id=user_id, page=page)
            await session.execute(stmt)
            await session.commit()

    @staticmethod
    async def insert_book_fragments(book: dict[int:tuple]):
        async with async_session() as session:
            for key, value in book.items():
                session.add(MinFragments(fragment_id=key, fragment=value))
            await session.commit()

    @staticmethod
    async def select_book_fragment(fragment_num):
        async with async_session() as session:
            result = await session.get(MinFragments, fragment_num)
            return result.fragment

    @staticmethod
    async def select_fragment_id(page):
        async with async_session() as session:
            result = await session.get(MinBookOrm, page)
            return result.fragment_id

    @staticmethod
    async def select_page_of_chapter(chapter_id):
        async with async_session() as session:
            stmt = select(func.min(MinBookOrm.page_id)).where(MinBookOrm.fragment_id == chapter_id)
            result = await session.execute(stmt)
            return result.scalar()

    @staticmethod
    async def insert_user_excerpt(text, name):
        async with async_session() as session:
            session.add(UserTextOrm(excerpt=text, user_name=name))
            await session.commit()


    @staticmethod
    async def select_random_excerpt(previous_num=None) -> tuple | None:
        """Возвращает случайный отрывок, за исключением предыдущего,
        если предыдущий имеется"""
        async with async_session() as session:
            random_num = previous_num

            stmt = select(UserTextOrm.id)
            lst_temp = await session.execute(stmt)
            all_excerpts = lst_temp.scalars().all()
            # если в базе ни одного отрывка или один то возвращаем None
            if (len(all_excerpts) == 0 or
                    (previous_num and len(all_excerpts) == 1)):
                return None

            # если имеется предыдущее число
            if previous_num:
                while random_num == previous_num:
                    random_num = choice(all_excerpts)
            else:
                random_num = choice(all_excerpts)
            result = await session.get(UserTextOrm, random_num)
            return result.excerpt, result.id, result.user_name

    @staticmethod
    async def insert_kabdict_definition(dct):
        """Добавляет в словарь строку: термин, перевод, объяснение"""
        async with async_session() as session:
            for term, translation, definition in dct.values():
                session.add(KabDictionary(term=term,
                                          translation=translation,
                                          definition=definition
                                          ))
            await session.commit()

    @staticmethod
    async def insert_term(term_tpl):
        async with async_session() as session:
            term, translation, definition = term_tpl
            session.add(KabDictionary(term=term,
                                      translation=translation,
                                      definition=definition
                                      ))
            await session.commit()


    @staticmethod
    async def select_all_dict_ids():
        async with async_session() as session:
            stmt = select(KabDictionary.id)
            result = await session.execute(stmt)
            return result.scalars().all()

    @staticmethod
    async def select_excerpt(excerpt_id):
        async with async_session() as session:
            result = await session.get(UserTextOrm, excerpt_id)
            return result.excerpt

    @staticmethod
    async def update_excerpt_rating(excerpt_id, step="up"):
        async with async_session() as session:
            excerpt = await session.get(UserTextOrm, excerpt_id)
            if step == "up":
                excerpt.rating += 1
            elif step == "down":
                excerpt.rating -= 1
            await session.commit()

    @staticmethod
    async def select_top_excerpts():
        async with async_session() as session:
            stmt = select(UserTextOrm).order_by(UserTextOrm.rating).limit(3)
            result = await session.execute(stmt)
            return result.scalars().all()


    @staticmethod
    async def select_specific_terms(lst: list[int]):
        async with async_session() as session:
            stmt = select(KabDictionary).where(KabDictionary.id.in_(lst))
            result = await session.execute(stmt)
            return result.scalars().all()



    @staticmethod
    async def insert_questionable_dct(user_id):
        async with async_session() as session:
            session.add(Questionable(object=str(usersdictplaycache[user_id])))
            await session.commit()

    @staticmethod
    async def insert_questionable_excerpt(report_text):
        async with async_session() as session:
            session.add(Questionable(object=report_text))
            await session.commit()
