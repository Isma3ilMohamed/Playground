package ktor_test


import io.ktor.client.*
import io.ktor.client.call.*
import io.ktor.client.engine.okhttp.*
import io.ktor.client.plugins.*
import io.ktor.client.plugins.contentnegotiation.*
import io.ktor.client.request.*
import io.ktor.client.statement.*
import io.ktor.serialization.kotlinx.json.*
import kotlinx.coroutines.runBlocking
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.Json

object Constants{
    const val CLIENT_ID_HEADER="client-id"
    const val CLIENT_ID="zgZg6SVtDzaknT6ddFwF2Ig96x3KzdwQFFokziaOM918aFDPcn"
    const val CLIENT_SECRET_HEADER="client-secret"
    const val CLIENT_SECRET="gmJXIRfHploja3WDUnR8LYmtS9sAE7cfUnTcvi3aKbLnOLsgLC"
}

val client = HttpClient(OkHttp) {
    install(ContentNegotiation) {
        json(Json {
            prettyPrint = true
            isLenient = true
            ignoreUnknownKeys = true
            explicitNulls=false
        })
    }

    defaultRequest {
        header(Constants.CLIENT_ID_HEADER,Constants.CLIENT_ID)
        header(Constants.CLIENT_SECRET_HEADER,Constants.CLIENT_SECRET)
        header("Authorization","Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2JlZml0LXN0YWdpbmctcmV2YW1wLnJvYnVzdGFzdHVkaW8uY29tL2FwaS9hdXRoL2xvZ2luL3Bob25lIiwiaWF0IjoxNzE3NTYyMTQ2LCJleHAiOjE3ODk1NjIxNDYsIm5iZiI6MTcxNzU2MjE0NiwianRpIjoicTBCMDlFaFJsb1AxR1JNZSIsInN1YiI6IjcxOTgyIiwicHJ2IjoiZjkzMDdlYjVmMjljNzJhOTBkYmFhZWYwZTI2ZjAyNjJlZGU4NmY1NSJ9.Hmtt-iymG9yPzhxFbUxPzPjAVQAVmP_7tmzVmOV37Xg")
    }
}

@Serializable
data class Arena(
    val id: Int,
    val name: String,
    val description: String?,
    val location: String,
    val google_maps_url: String,
    val latitude: Double,
    val longitude: Double,
    val cover: String,
    val thumbnails: List<String>
)

@Serializable
data class Response(
    val data: List<Arena>
)


suspend fun fetchArenas(): Response {
    val response: HttpResponse = client.get("https://befit-staging-revamp.robustastudio.com/api/arenas?get_all_arenas=true")
    val rawJson = response.bodyAsText()
    println(rawJson)  // Print the raw JSON response
    val dataResponse: Response = Json.decodeFromString(Response.serializer(), rawJson)
    return response.body()
}

fun main() {
    runBlocking {
        try {
            val arenas = fetchArenas()
            println(arenas)
        } catch (e: Exception) {
            e.printStackTrace()
        }
    }
}