# MPSS

MPSS is an implementation of the paper: <bold> Automated User Experience Testing through Multi-Dimensional Performance Impact Analysis </strong> at the <em> 2021 IEEE/ACM International Conference on Automation of Software Test (AST) </em>

### Abstract
Although there are many automated software testing suites, they usually focus on unit, system, and interface testing. However, especially software updates such as new security features have the potential to diminish user experience. In this paper, we propose a novel automated user experience testing methodology that learns how code changes impact the time unit and system tests take, and extrapolate user experience changes based on this information. Such a tool can be integrated into existing continuous integration pipelines, and it provides software teams immediate user experience feedback. We construct a feature set from lexical, layout, and syntactic characteristics of the code, and using Abstract Syntax Tree-Based Embeddings, we can calculate the approximate semantic distance to feed into a machine learning algorithm. In our experiments, we use several regression methods to estimate the time impact of software updates. Our open-source tool achieved a 3.7% mean absolute error rate with a random forest regressor.

### To cite
```
@article{biringaautomated,
  title={Automated User Experience Testing through Multi-Dimensional Performance Impact Analysis},
  author={Biringa, Chidera and Kul, G{\"o}khan}
}
```

