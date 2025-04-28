package com.tuzicao.emeraldknight.game

import android.content.Context
import com.tuzicao.emeraldknight.R
import org.json.JSONArray
import org.json.JSONObject
import org.xmlpull.v1.XmlPullParser
import org.xmlpull.v1.XmlPullParserFactory

class GameLogic {
    companion object {
        lateinit var ChoiceMap:HashMap<String,JSONObject>
        fun readJSONObject(context: Context,file_name:String):JSONObject{
            return JSONObject(context.assets.open(file_name).bufferedReader().use { it.readText() })
        }
        fun readJSONArray(context: Context,file_name:String): JSONArray {
            return JSONArray(context.assets.open(file_name).bufferedReader().use { it.readText() })
        }
        fun init(context: Context){
            var choices= readJSONArray(context,"choices.json")
            for(i in 0 until  choices.length()){
                var item=choices.getJSONObject(i)
                GameLogic.ChoiceMap.put(item.getString("id"),item)
            }
        }
        fun getSceneText(context:Context, sceneId: String): String? {
            try {
                val inputStream = context.resources.openRawResource(R.raw.scene_text)
                val parser = XmlPullParserFactory.newInstance().newPullParser()
                parser.setInput(inputStream, null)

                var eventType = parser.eventType
                var sceneText: String? = null
                var currentSceneId = ""

                while (eventType != XmlPullParser.END_DOCUMENT) {
                    when (eventType) {
                        XmlPullParser.START_TAG -> {
                            if (parser.name == "scene") {
                                currentSceneId = parser.getAttributeValue(null, "id")
                            } else if (parser.name == "text" && currentSceneId == sceneId) {
                                sceneText = parser.nextText()
                            }
                        }
                    }
                    eventType = parser.next()
                }
                return sceneText
            } catch (e: Exception) {
                e.printStackTrace()
                return null
            }
        }
    }
}