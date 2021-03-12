from manim import *




class Equations(Scene):

    def construct(self):
        title = Text("Quantization in PyTorch in 1:30s", font="Product Sans", size=1, gradient=(ORANGE, YELLOW)).scale(0.5).shift_onto_screen()
        self.play(Write(title))
        self.wait(1)
        text = MathTex(
            "Q(x, scale, zeroPoint) = round(\\frac{x}{scale} + zeroPoint)")
        quantization = Text("What is  Quantization in ML?", font="Product Sans", size=1, gradient=(ORANGE, BLUE)).scale(0.5)     
        quantization_ans = Text("Quantization is the process of performing computations and storing tensors at lower bitwidths or size than floating point precision. In essence, converting float32 to maybe float16 or int8,16 etc.", font="Product Sans", size=1, gradient=(BLUE, WHITE)).next_to(quantization, DOWN).scale(0.4)
        quantization_details = Text("PyTorch supports multiple approaches to quantizing a deep learning model. In most cases the model is trained in FP32 and then the model is converted to INT8.", font="Product Sans", size=1, gradient=(BLUE, WHITE)).next_to(quantization_ans, DOWN).scale(0.4)

        # VGroup(quantization, text).arrange(UP)
        self.play(
            FadeOutAndShift(title),
            ShowCreation(quantization, run_time=2),
            
        )
        self.play(
            ShowCreation(quantization_ans, run_time=3),
        )  
        self.play(
            ShowCreation(quantization_details, run_time=3),
        )
        

        self.wait(3)

                
        transform_title = Text("PyTorch supports two types of quantization, namely", gradient=(ORANGE, RED), font="Product Sans", size=1).scale(0.5)
        

        
        transform_title.to_corner(UP + LEFT)
        
        # text.to_corner(UP + RIGHT).scale(0.3)
        self.play(
        ReplacementTransform(quantization, transform_title),
        FadeOutAndShift(quantization_ans),
        FadeOutAndShift(quantization_details),
        )

        types_of_quants = Text("1. Eager Mode Quantization\n\n2. FX Graph Mode Quantization", gradient=(ORANGE, YELLOW), font="Product Sans", size=1).scale(0.4).next_to(transform_title, DOWN)
        self.play(Write(types_of_quants))

        self.wait(3)
        py1 = Text("1. Eager Mode Quantization", gradient=(ORANGE, YELLOW), font="Product Sans", size=1).scale(0.7)
        py1.to_corner(UP+LEFT)
        eager_mode = Text("Eager Mode Quantization is still a beta feature, you need to specify the composition of where quantization and dequantization happens manually, also it only supports modules and not functionals.", font="Product Sans", size=1).scale(0.4).next_to(py1, DOWN).shift_onto_screen()



        
        types_of_eager = Text("There are three types of quantization supported in Eager Mode Quantization", gradient=(ORANGE, YELLOW), font="Product Sans", size=1).scale(0.5).next_to(eager_mode, DOWN).shift_onto_screen()

        types_of_eager_list = Text("1. Dynamic quantization -  weights are quantized ahead of time but the activations are dynamically quantized during inference.\n\n\n2. Static quantization or Post Training Quantization(PTQ) - weights are quantized, activations are quantized, calibration required post training.\n\n\n3. Quantization aware training(QAT) weights are quantized, activations are quantized, quantization numerics modeled during training, giving higher accuracy during inference.", font="Product Sans", size=1).scale(0.4).next_to(types_of_eager, DOWN)

        self.play( 
            ReplacementTransform(transform_title, py1),
            FadeOutAndShift(types_of_quants),
            LaggedStart(Write(eager_mode), lag_ratio=3),
            
            )
        self.wait(0.5)
        self.play(
            LaggedStart(Write(types_of_eager), lag_ratio=3),
        )
        self.wait(0.5)
        self.play(
            LaggedStart(Write(types_of_eager_list), lag_ratio=3),
        )

        self.wait(6)

        # dq_code = Code("dq_code.py", run_time=1,
        #                 scale_factor=0.6,
        #                 line_spacing=0.2,
        #                 tab_width=4,
        #                 insert_line_no=False,
        #                 background="rectangle",
        #                 language='python',
        #                 generate_html_file=True)
        dq_code = Code(
            "dq_code.py",

            background_stroke_width=1,
            background_stroke_color=WHITE,
            insert_line_no=True,
            style=Code.styles_list[35],
            background="window",
            language="python",
            font='Menlo',
            corner_radius=0.2,

        ).scale(0.6).shift(0.5*DOWN)
        dynamic = Text("1. Dynamic Quantization", font="Product Sans", size=1).scale(0.4).next_to(py1, DOWN).shift_onto_screen()
        self.play(
            FadeOutAndShift(types_of_eager_list),
            FadeOutAndShift(types_of_eager),
            FadeOutAndShift(eager_mode),
            Write(dynamic),
            LaggedStart(Write(dq_code,), lag_ratio=15),
        )

        self.wait(5)

        static = Text("2. Static Quantization", font="Product Sans", size=1).scale(0.4).next_to(py1, DOWN).shift_onto_screen()

        static_code1 = Code(
            "staticqt1.py",

            background_stroke_width=1,
            background_stroke_color=WHITE,
            insert_line_no=True,
            style=Code.styles_list[35],
            background="window",
            language="python",
            font='Menlo',
            corner_radius=0.2,


        ).scale(0.4).move_to(np.array([-3.6, 0, 0]))

        static_code2 = Code(
            "staticqt2.py",

            background_stroke_width=1,
            background_stroke_color=WHITE,
            insert_line_no=True,
            style=Code.styles_list[35],
            background="window",
            language="python",
            font='Menlo',
            corner_radius=0.2,


        ).scale(0.4).move_to(np.array([3.6, 0, 0]))

        self.play(
            FadeOutAndShift(dynamic),
            FadeOutAndShift(dq_code),
            Write(static),
            LaggedStart(Write(static_code1, ), lag_ratio=15),
            LaggedStart(Write(static_code2, ), lag_ratio=15),
        )

        self.wait(5)

        qat = Text("3. Quantization Aware Training(QAT)", font="Product Sans", size=1).scale(0.4).next_to(py1, DOWN).shift_onto_screen()

        qat_code1 = Code(
            "qat1.py",

            background_stroke_width=1,
            background_stroke_color=WHITE,
            insert_line_no=True,
            style=Code.styles_list[35],
            background="window",
            language="python",
            font='Menlo',
            corner_radius=0.2,

        ).scale(0.4).move_to(np.array([-3.6, 0, 0]))

        qat_code2 = Code(
            "qat2.py",

            background_stroke_width=1,
            background_stroke_color=WHITE,
            insert_line_no=True,
            style=Code.styles_list[35],
            background="window",
            language="python",
            font='Menlo',
            corner_radius=0.2,

        ).scale(0.4).move_to(np.array([3.6, 0, 0]))

        self.play(
            FadeOutAndShift(static),
            FadeOutAndShift(static_code1),
            FadeOutAndShift(static_code2),
            Write(qat),
            LaggedStart(Write(qat_code1, ), lag_ratio=15),
            LaggedStart(Write(qat_code2, ), lag_ratio=15),
        )

        self.wait(5)

        py2 = Text("2. FX Graph Mode Quantization", gradient=(ORANGE, YELLOW), font="Product Sans", size=1).scale(0.7)
        py2.to_corner(UP + LEFT)
        fx_graph_mode = Text("FX Graph Mode Quantization is a new automated quantization framework, and currently it’s a prototype feature. It improves upon Eager Mode Quantization by adding support for functionals", font="Product Sans", size=1).scale(0.4).next_to(py2, DOWN).shift_onto_screen()

        self.play(
            ReplacementTransform(py1, py2),
            FadeOutAndShift(qat),
            FadeOutAndShift(qat_code1),
            FadeOutAndShift(qat_code2),
            LaggedStart(Write(fx_graph_mode))
        )

        types_of_fx = Text("The supported quantization types in FX Graph Mode Quantization are:", gradient=(ORANGE, YELLOW), font="Product Sans", size=1).scale(0.5).next_to(fx_graph_mode, DOWN).shift_onto_screen()
        ptq = Text("1. Post Training Quantization", font="Product Sans", size=1, gradient=(ORANGE, YELLOW)).scale(0.4).next_to(types_of_fx, DOWN).shift_onto_screen()
        types_of_fx_list_ptq = Text("1. Weight Only Quantization\n\n2. Dynamic Quantization\n\n3. Static Quantization", font="Product Sans", size=1).scale(0.3).shift_onto_screen().next_to(ptq, DOWN).shift_onto_screen()

        qat_fx = Text("2. Quantization Aware Training", font="Product Sans", size=1, gradient=(ORANGE, YELLOW)).scale(0.4).next_to(types_of_fx, 9*DOWN).shift_onto_screen()
        types_of_qat_fx = Text("1. Static Quantization", font="Product Sans", size=1).scale(0.3).next_to(qat_fx, DOWN).shift_onto_screen()



        self.play(
            LaggedStart(Write(types_of_fx)),
            Write(ptq),
            Write(types_of_fx_list_ptq),
        )
        self.wait(1)

        self.play(
            Write(qat_fx),
            Write(types_of_qat_fx)
        )

        self.wait(5)

        ptq_for_code = Text("1. Post Training Quantization (PTQ)", font="Product Sans", size=1).scale(0.4).next_to(py2, DOWN).shift_onto_screen()

        ptq1 = Code(
            "ptqfx.py",

            background_stroke_width=1,
            background_stroke_color=WHITE,
            insert_line_no=True,
            style=Code.styles_list[35],
            background="window",
            language="python",
            font='Menlo',
            corner_radius=0.2,

        ).scale(0.45).shift_onto_screen().center()

        qat_fx_2 = Code(
            "ptqfx2.py",

            background_stroke_width=1,
            background_stroke_color=WHITE,
            insert_line_no=True,
            style=Code.styles_list[35],
            background="window",
            language="python",
            font='Menlo',
            corner_radius=0.2,

        ).scale(0.5)


        self.play(
            ReplacementTransform(ptq, ptq_for_code),
            FadeOutAndShift(fx_graph_mode),
            FadeOutAndShift(types_of_fx),
            FadeOutAndShift(types_of_fx_list_ptq),
            FadeOutAndShift(qat_fx),
            FadeOutAndShift(types_of_qat_fx),
            LaggedStart(Write(ptq1)),
        )

        self.wait(8)
        qat_for_code = Text("2. Quantization Aware Training (QAT)", font="Product Sans", size=1).scale(0.4).next_to(py2, DOWN).shift_onto_screen()

        self.play(
            ReplacementTransform(ptq_for_code, qat_for_code),
            FadeOutAndShift(ptq1),
            LaggedStart(Write(qat_fx_2), lag_ratio=15)
        )

        self.wait(8)

        thankx = Text("Hope you liked it!", font="Product Sans", size=1, gradient=(ORANGE, BLUE)).scale(0.8)
        thankx.center()
        self.play(
            FadeOutAndShift(qat_for_code),
            FadeOutAndShift(qat_fx_2),
            ReplacementTransform(py2, thankx),

        )
        self.wait(1)

        # pytorch = Text("array=torch.heavyside()", font='mono')
        # c = Text(">>>import torch", font="mono", color=GREEN).scale(0.5)
        # code = Text(">>> input = torch.tensor([-1.5, 0, 2.0])", font="mono").scale(0.5).next_to(c, DOWN)
        # code2 = Text(">>> values = torch.tensor([0.5])", font="mono").scale(0.5).next_to(code, DOWN)
        # code3 = Text(">>> torch.heaviside(input, values)", font="mono").scale(0.5).next_to(code2, DOWN)
        # code4 = Text("OUTPUT -> tensor([0.0000, 0.5000, 1.0000])" , gradient = (BLUE, GREEN), font="mono").scale(0.5).next_to(code3, DOWN)
        # code5 = Text(">>> values = torch.tensor([1.2, -2.0, 3.5])", font="mono").scale(0.5).next_to(code4, DOWN)
        # code6 = Text(">>> torch.heaviside(input, values)", font="mono").scale(0.5).next_to(code5, DOWN)
        # code7 = Text("OUTPUT -> tensor([0., -2., 1.])", gradient = (BLUE, GREEN), font="mono").scale(0.5).next_to(code6, DOWN)
        
        # eg = VGroup()
        # eg.add(code, code2, code3, code4, code5, code6, code7).shift(1.2*UP)
        
        # self.play(
        #     LaggedStart(ShowCreation(code)),
        #     ShowPassingFlash(code.copy().set_color(YELLOW))
        # )
        # self.play(
        # LaggedStart(ShowCreation(code2)),
        # )
        # self.play(
        # LaggedStart(ShowCreation(code3)),
        # )
        # self.play(    
        #     LaggedStart(ShowCreation(code4)),
        # )
        # self.play(
        #     LaggedStart(ShowCreation(code5)),
        # )
        # self.play(
        #     LaggedStart(ShowCreation(code6)),
        # )
        # self.play(
        #     LaggedStart(ShowCreation(code7)),
        # )
        # self.wait(3)
        # # des1.shift(3*UP)
        # # des2.shift(2.5*UP)
        # # des3.shift(2*UP)
        # # self.play(Write(des1))
        # # self.play(Write(des2))
        # # self.play(Write(des3))
        # # self.play(Write(text))
        # # self.play(Write(pytorch))
        # # self.wait(10)