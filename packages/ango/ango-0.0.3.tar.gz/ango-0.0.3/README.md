SDK for developing custom plugins that can be integrated to Ango-Hub platform.

    from ango import plugin


    # Create callback function for your plugin. 
    # Input and output definitions are set on Ango-Hub on plugin register
    def callback(data):
        result = model(data)
        return result
    
    
    p = plugin.Plugin("<YOUR_PLUGIN_ID>", callback)
    
    plugin.run(p)