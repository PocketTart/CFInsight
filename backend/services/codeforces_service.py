import httpx


class CodeforcesService:

    BASE_URL = "https://codeforces.com/api"

    async def get_profile(self, handle: str):

        async with httpx.AsyncClient() as client:

            response = await client.get(
                f"{self.BASE_URL}/user.info",
                params={"handles": handle}
            )

        data = response.json()

        if data["status"] != "OK":
            raise Exception("User not found")

        return data["result"][0]

    async def get_contests(self, handle: str):

        async with httpx.AsyncClient() as client:

            response = await client.get(
                f"{self.BASE_URL}/user.rating",
                params={"handle": handle}
            )

        return response.json()["result"]

    async def get_submissions(self, handle: str):

        async with httpx.AsyncClient() as client:

            response = await client.get(
                f"{self.BASE_URL}/user.status",
                params={"handle": handle}
            )

        return response.json()["result"]